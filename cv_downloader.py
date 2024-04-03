import requests
import json
import re
import os
import tkinter as tk
from time import sleep
from threading import Thread

# This project is exclusively developed by https://github.com/TufayelLUS
# Tested as working on Windows 11 Home, 03 April, 2024
# Any problems with your LinkedIn account after using this program will not be any of my liabilities
# Contact me for software development offers: https://www.linkedin.com/in/tufayel-ahmed-cse


cookies = open('cookies.txt', mode='r', encoding='utf-8').read().split('\n')[0]
cv_save_folder = "CVs"
request_delay = 5
log_file = "logs.log"


def print_log(text):
    with open(log_file, "a") as f:
        f.write(text + "\n")


class CVDownloader():

    def __init__(self) -> None:
        pass

    def start(self):
        root = tk.Tk()
        root.title("LinkedIn CV Downloader - By Tufayel")
        root.geometry("800x600")
        root.resizable(False, False)
        label = tk.Label(
            root, text="LinkedIn CV Downloader - By Tufayel", font=("Helvetica", 20))
        label.pack(pady=20)
        intro_label = tk.Label(
            root, text="Download bulk CV in a short time! Get them saved in a specified folder!")
        intro_label.pack(pady=0)
        instruction_label = tk.Label(
            root, text="Enter LinkedIn profile links below, one per line. ex. https://www.linkedin.com/in/tufayel-ahmed-cse/")
        instruction_label.pack(pady=20)
        self.link_entry = tk.Text(root, width=60, height=10)
        self.link_entry.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)
        frame = tk.Frame(root)
        self.delay_var = tk.StringVar(frame)
        text_label = tk.Label(
            frame, text="Delay in seconds between each profile downloaded: ")
        text_label.pack(side=tk.LEFT)
        self.delay_slider = tk.Spinbox(
            frame, from_=1, to=60, width=5, textvariable=self.delay_var, state='readonly')
        self.delay_var.set(str(request_delay))
        self.delay_slider.pack(pady=20)
        frame.pack()
        self.download_button = tk.Button(
            root, text="Start Downloading CV", command=self.startProcessLinkThread)
        self.download_button.pack()
        self.link_entry.focus()
        self.status_bar = tk.Label(root, text="")
        self.status_bar.pack(pady=20)
        root.mainloop()

    def requestCV(self, profile_id, profile_link):
        link = "https://www.linkedin.com/voyager/api/graphql"
        params = {
            'action': 'execute',
            'queryId': 'voyagerIdentityDashProfileActionsV2.ca80b3b293240baf5a00226d8d6d78a1'
        }
        headers = {
            'Accept': 'application/vnd.linkedin.normalized+json+2.1',
            'Cookie': cookies,
            'Csrf-Token': re.findall(r'JSESSIONID="(.+?)"', cookies)[0],
            'Dnt': '1',
            'Referer': profile_link,
            'Sec-Ch-Ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': '"Windows"',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
            'X-Li-Lang': 'en_US',
            'X-Li-Page-Instance': 'urn:li:page:d_flagship3_search_srp_people_load_more;Ux/gXNk8TtujmdQaaFmrPA==',
            'X-Li-Track': '{"clientVersion":"1.13.9792","mpVersion":"1.13.9792","osName":"web","timezoneOffset":6,"timezone":"Asia/Dhaka","deviceFormFactor":"DESKTOP","mpName":"voyager-web","displayDensity":1.3125,"displayWidth":1920.1875,"displayHeight":1080.1875}',
            'X-Restli-Protocol-Version': '2.0.0',
        }
        data = {
            "variables": {
                "profileUrn": "urn:li:fsd_profile:{}".format(profile_id)
            },
            "queryId": "voyagerIdentityDashProfileActionsV2.ca80b3b293240baf5a00226d8d6d78a1",
            "includeWebMetadata": True
        }
        try:
            resp = requests.post(link, headers=headers,
                                 params=params, data=json.dumps(data)).json()
        except:
            print_log("Failed to open {}".format(link))
            return None
        try:
            cv_pdf_link = resp.get('data').get('data').get(
                'doSaveToPdfV2IdentityDashProfileActionsV2').get('result').get('downloadUrl')
        except:
            print_log("Error processing CV link")
            return None
        return cv_pdf_link

    def downloadCV(self, link, username):
        print_log("Downloading CV from {}".format(link))
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cookie': cookies,
            'Cache-Control': 'max-age=0',
            'Dnt': '1',
            'Referer': 'https://www.linkedin.com/in/{}/'.format(username),
            'Sec-Ch-Ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': '"Windows"',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        }
        try:
            resp = requests.get(link, headers=headers)
            with open(os.path.join(cv_save_folder, 'cv-{}.pdf'.format(username)), 'wb') as f:
                f.write(resp.content)
            print_log("CV saved as cv-{}.pdf".format(username))
        except:
            print_log("Failed to download CV")

    def getProfileID(self, link):
        if not link.lower().startswith('http'):
            link = 'https://' + link
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'max-age=0',
            'Cookie': cookies,
            'Dnt': '1',
            'Sec-Ch-Ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': '"Windows"',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        }
        try:
            resp = requests.get(link, headers=headers).text
        except:
            print_log("Failed to open {}".format(link))
            return False
        try:
            profile_id = re.findall(
                r'urn:li:fsd_memberRelationship:(.+?)\&quot;', resp)[0]
        except:
            print_log(
                "Could not parse profile ID for the profile {}".format(link))
            return False
        return profile_id

    def startProcessLinkThread(self):
        self.status_bar.config(text="Processing started...", fg='#000')
        thread = Thread(target=self.processLinks, args=())
        thread.start()

    def processLinks(self):
        self.download_button.config(state=tk.DISABLED)
        all_links = self.link_entry.get("1.0", tk.END)
        all_links = all_links.split("\n")
        all_links = [link.strip() for link in all_links if link.strip()]
        count_of_links = len(all_links)
        if count_of_links == 0:
            self.status_bar.config(text="Please insert links first!")
            self.download_button.config(state=tk.NORMAL)
            return
        for i, link in enumerate(all_links):
            self.status_bar.config(
                text="Processing link {}/{}".format(i+1, count_of_links))
            profile_id = self.getProfileID(link)
            if profile_id:
                download_link = self.requestCV(profile_id, link)
                if download_link is not None:
                    try:
                        username = link.split(
                            '/in/')[1].split('/')[0].split('?')[0]
                    except:
                        print_log(
                            "Username could not be extracted from the profile link")
                        continue
                    self.downloadCV(download_link, username)
            sleep(int(self.delay_var.get()))
        self.download_button.config(state=tk.NORMAL)
        self.status_bar.config(text="Processing finished.", fg='#008000')
        self.link_entry.delete("1.0", tk.END)


if __name__ == "__main__":
    if not os.path.exists(cv_save_folder):
        os.mkdir(cv_save_folder)
    downloader = CVDownloader()
    downloader.start()

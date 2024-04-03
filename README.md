# LinkedIn CV Downloader
A GUI-based(Graphical User Interface) Python automation software for downloading bulk LinkedIn CV from a list of profile links. Automation makes our lives easier. With this open source Python based software, you'll have the ability to automatically download CV of different LinkedIn profiles in a folder organized by their usernames. LinkedIn automatic CV downloader executable file is compiled for your easier convenience too that you can download from here.

# Interface Presentation
The main screen will look like this:<br><br>
<img src="https://raw.githubusercontent.com/TufayelLUS/LinkedIn-CV-Downloader/main/screenshots/ss1.png" />
<br><br>
Downloaded CVs folder will look like this after successful downloads of the CV from LinkedIn:<br><br>
<img src="https://raw.githubusercontent.com/TufayelLUS/LinkedIn-CV-Downloader/main/screenshots/ss2.png" />

# Features
* Allows any number of input profile links
* Customizable delay between multiple profiles downloaded (delay is limited to 1-60 seconds only), it defaults to 5 seconds every time you open it
* Saves a log file of what is happening in the background in a logs.log file
* Doesn't require any LinkedIn account details but live cookies from an existing LinkedIn browser session. This saves triggering the LinkedIn safety system in most scenarios.

# How to install this?
1. First, download Python software from Python's official website. Python 3.x only is supported. Download from <a href="https://python.org/downloads">here</a> or for a precise Python version, <a href="https://www.python.org/downloads/release/python-3118/">download this version</a> and scroll to the bottom to download the correct version based on your operating system and <b>make sure to tick on "Add to PATH" during installation in windows machines</b>
2. Now, from the start menu (Windows) or Applications list (Linux/Mac), search for Command Prompt (Windows) or terminal (on Mac/Linux) and copy-paste the command written below:
<pre>pip3 install requests</pre><br>
This will show some installation progress and will install the library eventually. If you see any pip warning, you may ignore that as that's optional.
* If pip doesn't get recognized as a command, please re-install Python with "Add python to executable path" enabled, or for Mac/Linux, run the command <code>apt-get install python3-pip</code>
3. Now check the Usage Guide section.

# Usage Guide 
1. Assuming that the Python software and the library required by this project are installed, time for the script execution. First, download the Python script of your choice and put it inside a folder.
2. Right-click on the Python script and select the option "Edit with IDLE". If you don't see this option, you have to figure that out yourself to fix the problem but a correct installation will show this option in the right-click menu.
3. Now, locate the <b>Run</b> menu and select <b>Run Module</b> and control the software using the GUI screen.

# How to collect cookies?
1. Login to LinkedIn from your Chrome browser(or your favorite one) and navigate to <a href="https://www.linkedin.com/company/linkedin/">https://www.linkedin.com/company/linkedin/</a>
2. Right-click anywhere on that page and select "Inspect".
3. Go to the "networks" tab and in the "Filter" input box, type "graphql" and refresh the web page again while keeping the networks tab open.
4. You will see some matches shown below. Click on that, locate the "Headers" tab, copy the value from the cookies Response header, and paste it into the cookies.txt file located in the same folder.
<img src="https://raw.githubusercontent.com/TufayelLUS/LinkedIn-Scraper/master/LinkedIn%20Lead%20Scraper%202024%20Edition/help.png" />

# Disclaimer
I hold no liability if your LinkedIn account faces any problem after using this program in any way. Please use it at your own risk. 

# Loved This Open Source Project?
Star the repository and share it with your friends who might need this. Keep this on watch for more updates! Follow my GitHub for more quality projects like this.

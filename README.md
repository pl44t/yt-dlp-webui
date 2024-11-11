
# Yt-dlp webui 

A yt-dlp Webui using python and flask.

version 2.1
- better ui than previous versions.



You can run the it using:
- The portable Windows app 
- Linux install
- Linux server install which is great to have in a homelab.
## Installation

### Windows

##### You will Need:
- python version 3.x
- the python package "flask"

##### Install:

- Head to the [Releases Tab](https://github.com/pl44t/yt-dlp-webui/releases) and look for the newest version of the Windows App.
- Download and extract the zip file
- Open the unzipped folder and run the app.py
- A terminal will open and tell to head you to [localhost:5000](http://localhost:5000) in your web browser, there you can download your videos!


### Linux

1. **Navigate to your desired directory** for the install

```bash
  cd path\to\your\desired\directory
```

2. **Setup a screen session** in terminal to keep the process running(optional)
```bash
  screen -S yt-dlp-webui
```

3. **Clone the repo**
```bash
  git clone https://github.com/pl44t/yt-dlp-webui.git
  cd yt-dlp-webui
```

4. **Setup a virtual environment** named yt-dlp-webui
```bash
python -m venv yt-dlp-webui
```
or depending on how your python is setup you may neeed to use 

```bash
python3 -m venv yt-dlp-webui
```
5. **Then activate the environment**

```bash
  source yt-dlp-webui/bin/activate
```

6. **Install flask and yt-dlp** to the python environment
```bash
  pip install flask yt-dlp
```

 7. **Edit the download paths**

	1. Edit the app.py file to download to the correct directory (use nano or any other editor)
	
	```bash
	  nano app.py
	```
	
	2. Head to line 8, you should see
	
	```py
	  BASE_DOWNLOAD_FOLDER = '/BASE/DIRECTORY/FOR/DOWNLOADS/'
	```
	
	3. Change '/BASE/DIRECTORY/FOR/DOWNLOADS/' to whatever path from root you want, for example:
	```py
	  '/media/Videos/YouTube/'
	```
	
	4. Edit the index.html
	```bash
	  nano templates/index.html
	```
	
	5. On line 69 (nice)
	```html
	  <input type="text" class="form-control" id="subdir" name="subdir" placeholder="Enter subdirectory under /BASE/DIRECTORY/FOR/DOWNLOADS/">
	```
	
	Change the '/BASE/DIRECTORY/FOR/DOWNLOADS/' text to whatever directory you chose in the previous step

#### Running the webui

Start the webui
```bash
python app.py
```
or depending on how your python is setup you may neeed to use 
```bash
python3 app.py
```

Then head to [localhost:5000](http://localhost:5000) to check if the webui is up and running.


To exit the screen session in the terminal but keep it running in the background press:

```bash 
  "Ctrl + a"
  and then 
  "d"
```

And to resume:

```bash 
  screen -r yt-dlp-webui
```
    
## Features

- Default Download Location:
	By default on Windows, downloads will go to C:\Users\Public\Downloads (where C is the drive letter where the application is running from).
	Videos will be downloaded to the specified subfolder within this location.

- Changing the Base Download Location:
	Navigate to the _internal folder inside the yt-dlp webui folder.
	Open the config.json file.
	Edit the "base_download_folder" value to your desired location. Ensure you use double backslashes \\ (e.g., \\New\\Download\\Location\\).

#### Additional checkbox options:
-	Download subtitles.
-	Download the video thumbnail.
-	Skip sponsored segments (integration with the SponsorBlock browser extension).



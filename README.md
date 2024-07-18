A yt-dlp Webui using python and flask to create a site.


How to Use:

  Requirements for Windows App:
    none - other than the downloaded zip from the releases tab.
    install instructions inside.
    have fun downloading!
    

  Requirements for install version:
    git, 
    python or python3,  
    ffmpeg(needed for choosing video/audio quality and for conversion)

  Linux:

    #navigate to your desired directory for the install
      cd path\to\your\desired\directory


    #setup a screen session in terminal to keep the process running(optional)
      screen -S yt-dlp-webui


    #clone the repo
      git clone https://github.com/pl44t/yt-dlp-webui.git
      cd yt-dlp-webui


    #setup a virtual environment named yt-dlp-webui
      python -m venv yt-dlp-webui |or| python3 -m venv yt-dlp-webui
      source yt-dlp-webui/bin/activate


    #install flaskand yt-dlp
      pip install flask yt-dlp


    #edit the download paths
      #edit the app.py file to download to the correct directory (use nano or any other editor)
        nano app.py
          #go to line 8, you should see
            BASE_DOWNLOAD_FOLDER = '/BASE/DIRECTORY/FOR/DOWNLOADS/'
          #change '/BASE/DIRECTORY/FOR/DOWNLOADS/' to whatever path from root you want

      #edit the index.html
        nano templates/index.html
          #on line 69 (nice)
            <input type="text" class="form-control" id="subdir" name="subdir" placeholder="Enter subdirectory under /BASE/DIRECTORY/FOR/DOWNLOADS/">
          #edit the /BASE/DIRECTORY/FOR/DOWNLOADS/ to whatever directory you chose in the previous step, this text will show up in the textbox in the webui where the user will enter a subdirectory to download to(optional)


    #start the webui
      python app.py |or| python3 app.py


    #go to localhost:5000 to test 


    #exit the screen session
      Ctrl + a
    #and to resume for debugging
      screen -r yt-dlp-webui
    


  Windows:

    #navigate to your desired directory for the install
      cd path\to\your\desired\directory

      
    #clone the repo
      git clone https://github.com/pl44t/yt-dlp-webui.git
      cd yt-dlp-webui


    #setup a virtual environment named yt-dlp-webui
      python -m venv yt-dlp-webui |or| python3 -m venv yt-dlp-webui
      yt-dlp-webui\Scripts\activate


    #install flask and yt-dlp
      pip install flask yt-dlp


    #edit the download paths
      #edit the app.py file to download to the correct directory (use notepad or any text editor)
        notepad app.py
          #go to line 8, you should see
            BASE_DOWNLOAD_FOLDER = '/BASE/DIRECTORY/FOR/DOWNLOADS/'
          #change '/BASE/DIRECTORY/FOR/DOWNLOADS/' to whatever path from the C drive you want

      #edit the index.html
        notepad templates/index.html
          #on line 69 (nice)
            <input type="text" class="form-control" id="subdir" name="subdir" placeholder="Enter subdirectory under /BASE/DIRECTORY/FOR/DOWNLOADS/">
          #edit the /BASE/DIRECTORY/FOR/DOWNLOADS/ to whatever directory you chose in the previous step, this text will show up in the textbox in the webui where the user will enter a subdirectory to download to(optional)


    #start the webui
      python app.py |or| python3 app.py
      

    #go to localhost:5000 to test 
    
    #!on exiting terminal the webui server will stop!

  

# Speech Transcriber
Takes audio files and transcribes them into text using the Google Speech Recognition API. Please try to stick to .wav files rather than .mp3 files as wav files have a better bitrate than mp3. This difference in bitrate alone shows the loss of quality when MP3s are compressed.
## Getting Started
First you want to clone the repo
You'll need [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed on your compuer
```
$ git clone https://github.com/deepakj718/Speech_recognition.git
```
Change to the directory where you saved the project and install all the required packages.
 ```
 $ pip install -r requirements.txt
 
# OR

$ pip3 install -r requirements.txt
 ```
 After all the packages are installed next is to get the web application running
  ```
  $ python3 app.py
  
  # OR depending on the python version you have installed
  
  $ python app.py
  ```
  Open your browser and go to the local host server [http://127.0.0.1:5000/](http://127.0.0.1:5000/) and get started transcribing!
  


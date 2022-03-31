
# Jarvis - A Personal Virtual Assistant [![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

Jarvis is a virtual assistant which can be used to automate your tasks.

As it uses Windows Speech Engine to talk, this programme can run only in Windows operating system.(Linux Support Will Come Soon!)

# What jarvis can do

1. It can speak<br>

2. It can recognize your voice(speech to text) , and wishes you <br>

3. It can search on Wikipedia via voice command<br>
4. It can send an Email via voice command<br>

5. It can open google, YouTube, Facebook , Twitter, Stackoverflow on Google Chrome via voice command<br>

6. It can play Music , open applications, tell time, replays to your i love you<br>

  
# Requirments
modules used
```
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import random

```

### Make sure that you have the latest version of Python installed.


### If You Get ```No Module Named PYAUDIO``` Error!

Download suitable version of PyAudio File: https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio

Then Open CMD/Terminal and type : C:\Users\Programs\Python\Python37\Scripts add "pip install" file location where you downloaded the PyAudio whl file.
```example:C:\Users\Programs\Python\Python37\Scripts>pip install C:\Users\Desktop\Projects\PyAudio-0.2.11-cp37-cp37m-win_amd64.whl```
  

- Be sure to change the application paths on jarvis.py otherwise it won't open Google Chrome and other Apps. <br>

##### This app is still in development stage! Be sure to star the repository to get future updates.

## PRE-REQUISITES
Your laptop with 3.6.x (onwards) python installed.

**NOTE:** Those with Linux and MacOSX would have Python installed by default, no action required.

Windows: Download the version for your laptop via https://www.python.org/downloads/

**NOTES**
In your preferred editor, make sure indentation is set to "4 spaces".

---

Don't Delete any Files or IT MAY CRASH THE PROGRAM!

## Run using Python3.8+
1. Clone or download repositiory: https://github.com/arevish/jarvis-Personal-Virtual-Assistant.git
2. In source folder, run `python3 'jarvis.py'` to start program, optionally, run with `--help` argument to see other runtime options.

### ThankYou!
TV-API
==================
This api allows you to control local TV.  Right now it is setup to work with Samsung using their serial ex-link attachement.  I use raspberry pi with a usb to 3.5mm serial adapter to connect to the ex-link samsung port and control the tv over serial.  This way I can work with very old all the way up to the latest version of samsung tvs.

## Run Locally
1) Install Python 2 and Pip on the box and place them in the path
2) run `pip install -r requirements.txt`
3) copy the config.ini.sample to config.ini and then modify the contents of the file to the desired configuration.
4) run `python serve.py`

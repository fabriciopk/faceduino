=========
Faceduino
=========

Faceduino is a Python interface for connect facebook to arduino.


Installation
============

If you install from source with "python setup.py install", don't forget to
install 'pyserial'.

    git clone https://github.com/fabriciopk/faceduino
    cd faceduino
    pip install faceduino
    python setup.py install

Usage
=====
- Set MY_TOKEN, a facebook token (https://developers.facebook.com/tools/explorer/)
- Set Arduino COM port
	board = Arduino(ARDUINO_PORT)
	fb = facebook(MY_TOKEN)
	print fb.fetchStatus(NAME_FRIEND)
	if (fb.fetchStatus(NAME_FRIEND)=='active'):
		board.blink(13)
		board.buzzer(22)
		board.delay(2)


Todo
====

-Implement a class to use internet shield for the connection betwen facebook and arduino
-Inplement facebook chat interations


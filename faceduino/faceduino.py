import urllib
import json
import serial
import time

class Facebook(object):
    def __init__(self, access_token):
        self.token = access_token
        self.url = 'https://graph.facebook.com/fql?access_token='+access_token+'&q='
    def fetchStatus(self,friend):
        self.query = 'SELECT online_presence FROM user WHERE username IN ("'+friend+'")'
        urlf = self.url + self.query
        request = self.__request(urlf)
        return self.__jsonStrip(request, 'online_presence')
    def getFriendUid(self, friend):
        self.query = 'SELECT uid FROM user WHERE username IN ("'+friend+'")'
        urlf = self.url + self.query   
        request = self.__request(urlf)
        return self.__jsonStrip(request, 'uid')
    def getFriendInfo(self, friend):
        self.query = 'SELECT uid, name, online_presence, status FROM user WHERE username IN ("'+friend+'")'
        urlf = self.url + self.query   
        return self.__request(urlf)
    def __request(self, url):
        resp = urllib.urlopen(url).read()
        return resp
    def __jsonStrip(self, string, field):
        self.parse = json.loads(string.decode('utf-8'))
        return self.parse['data'][0][field]
		

'''
# Python Arduino Prototyping API v2 - Copyright (c) 2009-2010 Akash Manohar J <akash@akash.im>
This is a project based on the original [Python Arduino Prototyping API v2]
'''

		
class Arduino(object):
    __OUTPUT_PINS = -1

    def __init__(self, port, baudrate=115200):
        self.serial = serial.Serial(port, baudrate)
        self.serial.write('99')

    def output(self, pinArray):
        self.__sendData(len(pinArray))

        if(isinstance(pinArray, list) or isinstance(pinArray, tuple)):
            self.__OUTPUT_PINS = pinArray
            for each_pin in pinArray:
                self.__sendData(each_pin)
        return True

    def setLow(self, pin):
        self.__sendData('0')
        self.__sendData(pin)
        return True
    def buzzer(self, pin):
        self.__sendData('5')
        self.__sendData(pin)
    def blink(self, pin):
        self.output([pin])
        for i in range(20):
            self.setHigh(pin)
            time.sleep(1)
            self.setLow(pin)
            time.sleep(1)
    def setHigh(self, pin):
        self.__sendData('1')
        self.__sendData(pin)
        return True

    def getState(self, pin):
        self.__sendData('2')
        self.__sendData(pin)
        return self.__formatPinState(self.__getData()[0])

    def analogWrite(self, pin, value):
        self.__sendData('3')
        self.__sendData(pin)
        self.__sendData(value)
        return True

    def analogRead(self, pin):
        self.__sendData('4')
        self.__sendData(pin)
        return self.__getData()

    def turnOff(self):
        for each_pin in self.__OUTPUT_PINS:
            self.setLow(each_pin)
        return True

    def __sendData(self, serial_data):
        while(self.__getData()[0] != "w"):
            pass
        self.serial.write(str(serial_data))

    def __getData(self):
        return self.serial.readline().rstrip('\n')

    def __formatPinState(self, pinValue):
        if pinValue == '1':
            return True
        else:
            return False
    def delay(self,secs):
        time.sleep(secs)
    def close(self):
        self.serial.close()
        return True
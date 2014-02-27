from faceduino import Arduino, Facebook

ARDUINO_PORT = ''#serial port
MY_TOKEN = ''
NAME_FRIEND = ''

board = Arduino(ARDUINO_PORT)
fb = facebook(MY_TOKEN)


while True:
    print fb.fetchStatus(NAME_FRIEND)
    if (fb.fetchStatus(NAME_FRIEND)=='active'):
        print fb.fetchStatus(NAME_FRIEND)
        for i in range(20):
            board.output([22,24])
            board.setHigh(22)
            board.buzzer(24)
            time.sleep(1)
            board.setLow(22)
            time.sleep(1)
    time.sleep(5)

board.close()
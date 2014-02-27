from faceduino import Arduino, Facebook

ARDUINO_PORT = 'COM12'
MY_TOKEN = 'CAACEdEose0cBAJp6NHHtISJDAZB3bcpilOzKaQxXcPYmuN7UYFHxX6d1aUbwjnueOlCX9doZBPjEuDUcpmpzvmeJsCmdlYcTDFx4oRG5lIcH7GL2ZAyiRjAsYkBY0eK599dA05ZA6ZACgXK2bYlZBeIEQtJ38fRpZCZCm5h3unhC102739ZAEg1uehGNhJzIeKQIZD'
NAME_FRIEND = 'wilian.padilha.7'

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
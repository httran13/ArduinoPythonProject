from pyfirmata import Arduino, util
from time import sleep
import os

port = '/dev/cu.usbmodem621'
board = Arduino(port)
sleep(5)

iterator = util.Iterator(board)
iterator.start()

analog0 = board.get_pin('a:0:i') #analog:pin:mode

try:
    while True:
        potentiameter = analog0.read()
        sleep(2)
        print potentiameter

except KeyboardInterrupt:
    board.exit()
    os._exit()



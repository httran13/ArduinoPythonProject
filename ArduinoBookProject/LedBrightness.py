from pyfirmata import Arduino, INPUT, PWM
from time import sleep
import random

port = '/dev/cu.usbmodem621'
board = Arduino(port)
sleep(5)

pin = 13
board.digital[pin].mode = PWM

for i in range (0, 99):
    r = random.randint(1,100)

    ledPin.write(r /100.00)
    sleep(0.1)
    ledPin.write(0)
    board.exit()


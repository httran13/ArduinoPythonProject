def dcMotorControl(r, deltaT):
    pwmPin.write(r/100.00)
    sleep(deltaT)
    pwmPin.write(0)

from pyfirmata import Arduino
from time import sleep
import os

port = '/dev/cu.usbmodem621'
board = Arduino(port)
sleep(5)

# set mode of pin 3 as PWM
pwmPin = board.get_pin('d:3:p')

try:
    while True:
        r = input("Enter value to set motor speed: ")
        if ( r > 100) or ( r <= 0 ) :
            print "betwee 0 to 100 only"
            board.exit()
            break
        t = input("How long? in seconds")
        dcMotorControl(r, t)
except KeyboardInterrupt:
    board.exit()
    os._exit



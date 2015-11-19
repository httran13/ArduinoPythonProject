#!/huy/bin/python

# Import lib
import pyfirmata
from time import sleep


# cus functions
def blinkLed(pin, message):
    print message
    board.digital[pin].write(1)
    sleep(1)
    board.digital[pin].write(0)
    sleep(1)


# associate port and board with pyfirmata
port = '/dev/cu.usbmodem621'
board = pyfirmata.Arduino(port)

# Use iterator thread to avoid buffer overflow
it = pyfirmata.util.Iterator(board)
it.start()


# define pins
pirPin = board.get_pin('d:7:i')
redPin = 12
greenPin = 13

# Check for pir sensor input

while True:
    value = pirPin.read()

    if value is True:
        blinkLed(redPin, "Motion detecte")


    else:
        # perform blink
        print "in else"
        blinkLed(greenPin, "No motion")

# release board
board.exit()

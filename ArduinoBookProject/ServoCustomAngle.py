from pyfirmata import Arduino, SERVO
from time import sleep

port = '/dev/cu.usbmodem621'
board = Arduino(port)
sleep(5)

# set mode of pin
pin = 13
board.digital[pin].mode = SERVO

#custom method

def setServoAngle(pin, angle):
    board.digital[pin].write(angle)
    sleep(0.015)


#testing the function by rotating motor in both directions
while True:
    for i in range(0, 180):
        setServoAngle(pin, i)
    for i in range(180, 1, -1):
        setServoAngle(pin, i )

    #continue or break the testing process

    i = raw_input("Enter 'y' to continue or Enter to quit): ")
    if i == 'y':
        pass
    else:
        board.exit()
        break
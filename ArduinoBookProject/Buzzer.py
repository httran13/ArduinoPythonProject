from pyfirmata import Arduino
from time import sleep



def buzzerPattern(pin, recurrence, pattern):
    pattern1 = [0.8, 0.2]
    pattern2 = [0.2, 0.8]
    flat = True

    for i in range(recurrence):
        if pattern == 1:
            p = pattern1
        elif pattern == 2:
            p = pattern2
        else:
            print "Please enter valid pattern. 1 or 2."
            exit
        for delay in p:
            if flat is True:
                board.digital[pin].write(1)
                flag = False
                sleep(delay)
            else:
                board.digital[pin].write(0)
                flat = True
                sleep(delay)

    board.digital[pin].write(0)
    board.exit()


port = '/dev/cu.usbmodem621'
board = Arduino(port)
sleep(5)

buzzerPattern(2, 10, 1)


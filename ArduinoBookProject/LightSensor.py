import time
from PyMata.pymata import PyMata

port = PyMata("/dev/cu.usbmodem621")
port.i2c_config(0, port.ANALOG, 4, 5)
addr = 0x23
#Request bh to send 2 bytes
port.i2c_read(addr, 0, 2, port.I2C_READ)

#wait for bh to send the data
time.sleep(3)

#read data from bh
data = port.i2c_get_read_data(addr)

#Obtain lux values from received data
LuxSum = (data[1] << 8 | data[2]) >> 4

lux = LuxSum / 1.2
print str(lux) + ' lux'

firmata.close()


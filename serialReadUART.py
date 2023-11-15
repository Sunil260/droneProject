'''
UART communication on Raspberry Pi using Pyhton
http://www.electronicwings.com
'''
import serial
from time import sleep

ser = serial.Serial ("/dev/ttyS0", 420000, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE);  #Open port with baud rate
#
print(ser.name);


data = ser.read(26).hex();
print(len(data));
data = data[6:50];


# while True:
#     received_data = ser.read()              #read serial port
#     sleep(.5)
#     data_left = ser.inWaiting()             #check for remaining byte
#     received_data += ser.read(data_left)
#     print (received_data)                   #print received data
#     ser.write(received_data)   


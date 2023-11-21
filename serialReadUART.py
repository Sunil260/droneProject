'''
UART communication on Raspberry Pi using Pyhton
http://www.electronicwings.com
'''
import serial
from time import sleep

ser = serial.Serial ("/dev/serial0", 420000, bytesize=8, timeout=0.2, stopbits=serial.STOPBITS_ONE);  #Open port with baud rate

ser2 = serial.Serial("/dev/ttyAMA3",115200, bytesize=8, timeout=0.2, stopbits=serial.STOPBITS_ONE);

# print(ser2.name);

def portSetup():

    rc_To_Pi = serial.Serial ("/dev/serial0", 420000, bytesize=8, timeout=0.2, stopbits=serial.STOPBITS_ONE);  #Open port with baud rate
    pi_to_Fc = serial.Serial("/dev/ttyAMA3",115200, bytesize=8, timeout=0.2, stopbits=serial.STOPBITS_ONE);

    return [rc_To_Pi, pi_to_Fc]

def close_Ports([serialPorts]):
    for port in serialPorts:
        port.close()
    return True

def readFc(portFC):
    while True:
        received_data = portFC.read()              #read serial port
        sleep(.5)
        data_left = portFC.inWaiting()             #check for remaining byte
        received_data += portFC.read(data_left)
        print (received_data)    
    
    return  
                 #print received data
def readRc(portRc):

    while True:  
        received_data = portRc.read()              #read serial port
        sleep(.5)
        data_left = portRc.inWaiting()             #check for remaining byte
        received_data += portRc.read(data_left)
        print (received_data)    
    
    return 

def rwRctoFc(portFC,portRc):

    while True:
        received_data = portRc.read()              #read serial port
        sleep(.5)
        data_left = portRc.inWaiting()             #check for remaining byte
        received_data += portRc.read(data_left)
        print (received_data)                   #print received data
        portFC.write(received_data)   

def main():
    portRc, portFc = portSetup()
    

if __name__ == “__main__”:
         main()

# data = ser.read(26).hex();
# print(len(data));
# data = data[6:50];
# data = int(data, 16);
# print(data);

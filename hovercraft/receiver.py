import socket
import sys
import os     #importing os library so as to communicate with the system
import time   #importing time library to make Rpi wait because its too impatient 
os.system ("sudo pigpiod") #Launching GPIO library
time.sleep(1) # As i said it is too impatient and so if this delay is removed you will get an error
import pigpio #importing GPIO library


#TODO: Blink LED

leftMotor = 5
rightMotor = 13

pi = pigpio.pi()
pi.set_servo_pulsewidth(leftMotor, 1000)
pi.set_servo_pulsewidth(rightMotor, 1000)

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('192.168.0.68', 10000)
print ('starting up on %s port %s' % server_address)
sock.bind(server_address)

while True:
    print('waiting to receive message')
    data, address = sock.recvfrom(4096)

    print('received %s bytes from %s' % (len(data), address))
    print(data)

    motorSpeeds = data.split()
    pi.set_servo_pulsewidth(leftMotor, int(motorSpeeds[0])
    pi.set_servo_pulsewidth(rightMotor, int(motorSpeeds[1])

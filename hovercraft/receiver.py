import socket
import sys

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

#!/usr/bin/python3
import socket
import sys

# Create a UDS socket
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
SOCKET = '/tmp/blinkt'
try:
    sock.connect(SOCKET)
except OSError:
    sys.exit(1)

try:
    message = ' '.join(sys.argv[1:])
    sock.sendall(message.encode())
    sock.close()
finally:
    sock.close()

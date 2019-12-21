#!/usr/bin/python3
import time
import socket
import os
import threading
import sys
# blinkt!
from blinkt import set_pixel, set_brightness, show

# Socket
SOCKET='/tmp/blinkt'

# Defaults
STATUSID=7

# Create a UDS socket
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

# COLOR Positions
R=0
G=1
B=2

# STATUS Array
STATUS=[[0,1,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]

# Show Status with STATUS array data
def setblinkt():
    global STATUS
    for i in range(8):
        set_pixel(i, STATUS[i][R], STATUS[i][G], STATUS[i][B])
    show()

# timed action
def timed():
    global STATUS,STATUSID
    i=0
    while True:
        i=(i+1)%2
        STATUS[STATUSID][G]=i
        setblinkt()
        time.sleep(1)

# Get commands from socket
def socketd():
    global STATUS,STATUSID
    # Definitionen
    SSHID=1
    WIFIID=2
    sock.listen(1)
    while True:
        setblinkt()
        connection, client_address = sock.accept()
        try:
            data = connection.recv(16).decode()
            #print( 'received "%s"' % data)
            if data == 'SSH':
                STATUS[SSHID][R]=0
                STATUS[SSHID][G]=1
                STATUS[SSHID][B]=0
                continue
            if data == 'WIFI_AP':
                STATUS[WIFIID][R]=0
                STATUS[WIFIID][G]=1
                STATUS[WIFIID][B]=0
                continue
            if data == 'WIFI_CLIENT':
                STATUS[WIFIID][R]=0
                STATUS[WIFIID][G]=0
                STATUS[WIFIID][B]=1
                continue
            # direct LED access
            if data.startswith('LED'):
                p = data.split()
                if len(p) != 5:
                    #print ('invalid data len %d', len(p))
                    continue
                l = int(p[1])
                r = int(p[2])
                g = int(p[3])
                b = int(p[4])
                STATUS[l][R]=r
                STATUS[l][G]=g
                STATUS[l][B]=b
                continue
        finally:
            connection.close()

# Main program / daemon
if __name__ == "__main__":
    # blinkt
    set_brightness(0.1)
    # Socket
    # make sure the socket does not already exist
    try:
        os.unlink(SOCKET)
    except OSError:
        if os.path.exists(SOCKET):
            raise
    # bind socket
    sock.bind(SOCKET)
    # Update blinkt
    t = threading.Thread(target=timed)
    t.daemon = True
    t.start()
    # get socket data
    socketd()

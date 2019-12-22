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

# Constants
SSHID=1
WIFIID=2
STATUSID=7
# COLOR Positions
R=0
G=1
B=2

# Create a UDS socket
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

# STATUS Array
status=[[0,1,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
statusold=[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]

# test array difference
def isdiff(a,b):
    """Is there a difference between two arrays of 3"""
    return a[0]!=b[0] or a[1]!=b[1] or a[2]!=b[2]

# Show Status with STATUS array data
def setblinkt():
    """Set blinkt LEDs if necessary"""
    global status
    changed=False
    for i in range(8):
        if isdiff(status[i],statusold[i]):
            changed=True
            set_pixel(i, status[i][R], status[i][G], status[i][B])
            statusold[i] = [status[i][R], status[i][G], status[i][B]]
    # update if changed
    if changed:
        show()

# timed action
def timed():
    """Timed updates (status)"""
    global status
    i=0
    while True:
        i=(i+1)%2
        status[STATUSID][G]=i
        setblinkt()
        time.sleep(5)

# Get number from string with upper and lower limit
def getint(st, low, up):
    """Get integer in given range"""
    c = int(st)
    if (c<low): c=low
    if (c>up): c=up
    return c

# Get color from string
def getcol(st):
    """Get color"""
    return getint(st,0,254)

# Get led number from string
def getled(st):
    """Get LED number"""
    return getint(st,0,7)

# Set LED status
def setled(l,r,g,b):
    """Set LED (l) colors r,g,b"""
    global status
    status[l][R]=0
    status[l][G]=1
    status[l][B]=0

# Get commands from socket
def socketd():
    """Socket communication"""
    sock.listen(1)
    while True:
        setblinkt()
        connection, client_address = sock.accept()
        try:
            data = connection.recv(16).decode()
            #print( 'received "%s"' % data)
            if data == 'SSH':
                setled(SSHID,0,1,0)
                continue
            if data == 'WIFI_AP':
                setled(WIFIID,0,1,0)
                continue
            if data == 'WIFI_CLIENT':
                setled(WIFIID,0,0,1)
                continue
            # direct LED access
            if data.startswith('LED'):
                p = data.split()
                if len(p) != 5:
                    #print ('invalid data len %d', len(p))
                    continue
                l = getled(p[1])
                r = getcol(p[2])
                g = getcol(p[3])
                b = getcol(p[4])
                setled(l,r,g,b)
                continue
        finally:
            connection.close()

# Main program / daemon
if __name__ == "__main__":
    # blinkt
    set_brightness(0.1)
    # Socket - make sure the socket does not already exist
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

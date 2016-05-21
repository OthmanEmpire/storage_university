#!/usr/bin/env python
# simple illustration client/server pair; 

# this is the client

import socket
import sys

print ('Usage is ./tcpclient <serverMachine> <portNumber> <message>')

# create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to server
host = sys.argv[1] # server address
port = int(sys.argv[2]) # server port
s.connect((host, port))

s.send((sys.argv[3]).encode()) # send test string

# read echo
data = (s.recv(1000)).decode() # read up to 1000 bytes
print (data)
print ('received', len(data), 'bytes')

 # close the connection
s.close()


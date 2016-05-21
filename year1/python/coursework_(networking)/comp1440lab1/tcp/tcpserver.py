#!/usr/bin/env python

# simple illustration client/server pair; client program sends a string
# to server, which echoes it back to the client (in multiple copies),
# and the latter prints to the screen

# this is the server

import socket
import sys

# create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# associate the socket with a port
host = '' # can leave this blank on the server side
port = int(sys.argv[1])
s.bind((host, port))

# accept "call" from client
print ('Waiting for incoming calls ...')
s.listen(1)
conn, addr = s.accept()
print ('client is at', addr)

# read string from client and make multiple copies 

data = (conn.recv(1000)).decode()
print ('received', data)


data = 10 * data # concatenate data with itself 9 times



# wait for the go-ahead signal from the keyboard (to demonstrate that
# recv() at the client will block until server sends)
print ('press a key to continue ...')
z = input()

# now send
conn.send(data.encode())

print ('done!')

# close the connection
conn.close()


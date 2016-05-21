#!/usr/bin/env python
# UDP Example - udpclient.py

import socket, sys, time

# Usage is ./udpclient <serverMachine> <portNumber>

host = sys.argv[1]
textport = sys.argv[2]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    port = int(textport)
except ValueError:
    # That didn't work.  Look it up instread.
    port = socket.getservbyname(textport, 'udp')

s.connect((host, port))
print ("Enter data to transmit: ")
data = sys.stdin.readline().strip()
s.sendall(data.encode())
s.shutdown(1)
print ("Looking for replies; press Ctrl-C or Ctrl-Break to stop.")
while 1:
    buf = s.recv(2048).decode()
    if not len(buf):
        break
    print ("Received: %s" % buf)

#!/usr/bin/env python
# UDP Echo Server - udpserver.py
import socket, traceback

host = ''                               # Bind to all interfaces
port = 51423

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))

print ("Server running ... listening on port", port)
 
while 1:
    try:
        message, address = s.recvfrom(8192)
        print ("Got ", message.decode(), " from", address)
        # Echo it back
        s.sendto(message, address)
    except (KeyboardInterrupt, SystemExit):
        raise
    except:
        traceback.print_exc()


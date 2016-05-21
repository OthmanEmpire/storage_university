#!/usr/bin/env python
# DNS - basic getaddrinfo() example - getaddrinfo-basic.py

import sys, socket

result = socket.getaddrinfo(sys.argv[1], None)
print (result[0][4])

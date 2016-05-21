#!/usr/bin/env python
# Basic Connection Example - connect1.py

import socket
import time

loops = 5
total_time_elapsed = 0
SERVER = "www.stackoverflow.com"

for n in range(1, loops + 1):

    # print ("Creating socket...",)
    start = time.perf_counter()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # print ("done.")

    # print ("Connecting to remote host...",)
    try:
        s.connect((SERVER, 80))
    except Exception as e:
        print("Unable to connect! Error: {} {}".format(type(Exception), e))
    end = time.perf_counter()
    # print ("done.")

    elapsed = end - start
    total_time_elapsed += elapsed
    print("ATTEMPT {}--Time taken to connect to {}: {}"
          .format(n, SERVER, elapsed))


avg = total_time_elapsed/loops

print("\nAverage time taken: {}".format(avg))
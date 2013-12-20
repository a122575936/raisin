#!/usr/bin/env python

"""
A simple echo client
"""

import socket

host = 'localhost'
port = 7000
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
print "connect successfully"
s.send('Hello, world\r\n')
data = s.recv(size)
s.close()
print 'Received:', data

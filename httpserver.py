#!/usr/bin/env python3

import sys
import socket

encoding_standard = 'ISO-8859-1'

if len(sys.argv) > 2:
    print('usage: webserver.py <port>')

port = 28333
if len(sys.argv) == 2:
    port = int(sys.argv[1])

print(sys.argv)
print(port)

response = 'HTTP/1.1 200 OK\n'
response += 'Content-Type: text/plain\n'
response += 'Content-Length: 6\n'
response += 'Connection: close\n'
response += '\n'
response += 'Hello!'

response = response.encode(encoding_standard)

s = socket.socket()

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind(('0.0.0.0', port))

s.listen()

while(1):
    new_conn = s.accept()
    new_socket = new_conn[0]

    request = new_socket.recv(4096).decode(encoding_standard)
    while '\r\n\r\n' not in request:
        request += new_socket.recv(4096).decode(encoding_standard)
    
    new_socket.sendall(response)
    new_socket.close()

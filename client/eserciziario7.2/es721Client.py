#!/usr/bin/env python3
import socket
import sys


if len(sys.argv)!= 2:
    print("ERROR: the function accept 1 parameter(hostname)")
    sys.exit(1)

HOST=sys.argv[1]
PORT=2525

#creo socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #creo connessione
    s.connect((HOST,PORT))
    print("Connession established...")
    #fai cose
    #data= s.recv(256)
    #print(data.decode('utf-8'))
    message="Connection from "+ socket.gethostname()
    s.sendall(message.encode('utf-8'))
    print("Closing connection...")
    #chiudo la connessione
    s.close()

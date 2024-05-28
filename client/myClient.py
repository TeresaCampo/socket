#!/usr/bin/env python3
import socket
import sys


if len(sys.argv)!= 3:
    print("ERROR: the function accept two ordered parameters(hostname,port)")
    sys.exit(1)

HOST=sys.argv[1]
PORT=int(sys.argv[2])

#creo socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket:
    #creo connessione
    socket.connect((HOST,PORT))
    print("Connession established...")
    #fai cose
    print("Closing connection...")
    #chiudo la connessione
    socket.close()

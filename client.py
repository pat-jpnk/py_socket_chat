#!/usr/bin/env python3

import socket 
import time 

header = 64
response = 512

port = 7002

disconnect_msg = "!disconnect"
server = socket.gethostbyname(socket.gethostname())
addr = (server, port)
msg_format = 'utf-8'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(addr)

def send(msg):
    msg = msg.encode(msg_format)
    msg_length = len(msg)
    send_length = str(msg_length).encode(msg_format)
    send_length += b' ' * (header - len(send_length))
    client.send(send_length)
    client.send(msg)
    print(client.recv(response).decode(msg_format))
    

def start():
    while True:
        msg = input()
        if (msg == '!disconnect'):
            send(str(msg))
            client.close()
            return 0
        send(str(msg))


start()
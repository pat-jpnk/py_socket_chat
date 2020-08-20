#!/usr/bin/env python3

# Add names for users joining ## DONE!
# Add global chat log

import socket 
import threading

header = 256
port = 1994

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
    client.send(send_length)
    client.send(msg)


def authenticate():
    complete = False

    while (not complete):
        print(client.recv(header).decode(msg_format))
        name = str(input())
        send(name)
        response = client.recv(header).decode(msg_format)
        if ((response.strip()) == "[+] name valid"):
            print(response.strip())
            complete = True
        else:
            print(response.strip())    

def start():

    # get client name
    authenticate()
    
    while True:
        msg = str(input())
        if (msg == disconnect_msg):
            send(msg)
            client.close()
        elif (len((msg).strip()) == 0) or msg.strip() == '\n':
            pass
        else:
            send(msg)


if __name__ == "__main__":
    start()
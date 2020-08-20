#!/usr/bin/env python3

import socket
import threading

header = 64
port = 7002

server_agent = socket.gethostbyname(socket.gethostname())
addr = (server_agent, port)

msg_format = 'utf-8'
disconnect_msg = '!disconnect'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(addr)

def handle_client_agent(conn, addr):
    print(f'[+] new connection: {addr}')

    connected = True
    while connected:
        msg_length = conn.recv(header).decode(msg_format)
        if (msg_length):
            msg_length = len(msg_length)
            print("MSLEN:",msg_length)
            msg = conn.recv(msg_length).decode(msg_format)
        
            if (msg == disconnect_msg):
                print(f"[-] {addr} disconnected")
                connected = False

            #addr[0]
            print(f'{addr} > {msg}') 
            conn.send(("Msg received").encode(msg_format))
    
    conn.close()    


def start_server():
    server.listen() 
    
    print(f'[+] server listening on {server_agent}')

    while True:
        (conn, addr) = server.accept()
        thread = threading.Thread(target=handle_client_agent, args=(conn,addr))
        thread.start()
        print(f'[+] active connections: {threading.activeCount() - 1}')


print('[+] starting server...')   
start_server()

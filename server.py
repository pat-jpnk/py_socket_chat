#!/usr/bin/env python3

# Add names for users joining
# Add global chat log

import socket
import threading
import defaultdict

header = 256
port = 1994

server_agent = socket.gethostbyname(socket.gethostname())
addr = (server_agent, port)

msg_format = 'utf-8'
disconnect_msg = '!disconnect'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(addr)

# Active users (name, conn)
connections = dict()

def validate_name(name,size):
    name = name.strip()
    if((size == 0) or (name in users)):
        return False
    else:
        return True


def authenticate_client(conn, addr):
    valid = False
    name = None

    while(not valid):
        conn.send(("Enter a name: ").encode(msg_format))
        name_size = conn.recv(header).decode(msg_format)
        name = str(conn.recv(header).decode(msg_format))
        
        print("NAME: ", name)

        if(validate_name(name,name_size)):
            conn.send(("[+] name valid").encode(msg_format))
            users.append((name,conn))
            valid = True
        else:
            conn.send(("[-] name invalid").encode(msg_format))

    return str(name)    


def broadcast(client_name, msg):
    while True:
        try:


        except:




def handle_client_agent(conn, addr):

    print("conn: ", conn)

    client_name = authenticate_client(conn,addr)
    connected = True

    while connected:
        print("USERS: ",users)
        msg_length = int(conn.recv(header).decode(msg_format))

        if (msg_length):
            msg = str(conn.recv(header).decode(msg_format))
        
            if (msg == disconnect_msg):
                print(f"[-] {addr} disconnected")
                connected = False
            broadcast(client_name, msg)    
           #print(f'{client_name} > {msg}')
    
    conn.close()    


def start_server():

    server.listen() 
    print(f'[+] server listening on {server_agent}')

    while True:
        (conn, addr) = server.accept()
        thread = threading.Thread(target=handle_client_agent, args=(conn,addr))
        thread.start()
        print(f'[+] active connections: {threading.activeCount() - 1}')


if __name__ == "__main__":
    print('[+] starting server...')   
    start_server()

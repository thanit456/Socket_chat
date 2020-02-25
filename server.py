import socket
from _thread import * 
import threading

def connection_func(con, addr):
    print('Connection : ', con)
    
    while True:
        data = con.recv(1024)
        print('received {!r}'.format(data))
        if data:
            print('sending message back to the client')
            if data[:3] == b'REG':
                username = data[3:].decode()
                username_dc[addr] = username
                print('GOT USERNAME : ', username)
                print(username_dc)
                message = data[3:] + b'is connected'
            else: 
                message = 'server got data'    
            con.sendall(data)
        else:
            print('no data from', addr)
            break
    con.close()

# global variables 
username_dc = dict()

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
# server_address = ('localhost', 10000)
# print('Starting up on {} port {}'.format(*server_address))
sock.bind(('', 50007))

# Listen for incoming connections
sock.listen(10)

# Blocking
sock.setblocking(1)

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
  
    print('connection from', client_address)
    start_new_thread(connection_func, (connection, client_address, ))
    # connection_func(connection, client_address)
    # Clean up the connection
print("Closing socket")
sock.close()
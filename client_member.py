import socket 
import sys



# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
# server_address = ('localhost', 10000)
# print('connecting to {} port {}'.format(*server_address))
# sock.connect(server_address)
sock.connect(('localhost', 50007))
try:
    username = input("Please input username : ").strip()
    register_message = b'REG' + username.encode('utf-8')
    sock.sendall(register_message)

    connected_message = sock.recv(16)
    if connected_message is not None:
        print('{!r}'.format(connected_message))
    else:
        print('Cannot connect')
        sys.exit(1)
    while True :
        message = (input(username + '>').strip()).encode('utf-8')
        print(message)
        if message == b'exit':
            break

        # Send data
        print('sending {!r}'.format(message))
        sock.sendall(message)

        # Look for the response
        amount_received = 0
        amount_expected = len(message)

        while amount_received < amount_expected:
            data = sock.recv(16)
            amount_received += len(data)
            print('received {!r}'.format(data))
finally:
    print('closing socket')
    sock.close()










# # global variables
# chat_room_name


# def menu():
#     print('-----------------------')
#     print('(1) See chat list')
#     print('(2) Create chat room ')
#     print('(3) Join chat room')
#     print('-----------------------')

# def get_chat_room():
#     chat_room_name = input('Please input chat room name : ').strip()
#     return chat_room_name

# while True:
#     select_menu = input('Please select the choice number : ').strip()
#     if select_menu == '1':
#         pass 
#     elif select_menu == '2':
#         chat_room_name = get_chat_room()
        
#         break
#     elif select_menu == '3':
#         chat_room_name = get_chat_room()
#         break

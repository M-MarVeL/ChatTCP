import socket

BUFFER = 1024
PORT = 5000

def server():
    host = socket.gethostname()
    client_socket = socket.socket() ## Instatiate
    client_socket.connect((host, PORT)) ## Connect to the server

    client(client_socket)

   

def client(client_socket):

    username = input("Insert your name -> ")
    msg = data(client_socket, username)

    while msg.lower().strip() != 'bye':

        message(client_socket)

        msg = data(client_socket, username)
    
    client_socket.close()


def message(client_socket):

    buffer = client_socket.recv(BUFFER).decode() ## Receive message from the server
    name = buffer[buffer.find("<") + 1:buffer.find(">")] ## 
    msg = buffer[buffer.find(":") + 1:]

    if not buffer:
        ## If buffer empty break
        return 0

    print(name + ": " + msg)


def data(connection, username): 
    data = input(" -> ")
    buffer = (f"<{username}>:{data}")
    if data.lower().strip() != 'bye':
        connection.send(buffer.encode())

    return data

if __name__ == '__main__':
    server()
import socket
import server

BUFFER = 1024
PORT = 5000

def client():
    host = socket.gethostname()
    client_socket = socket.socket() ## Instatiate
    client_socket.connect((host, PORT)) ## Connect to the server

    name = input("Insert your name -> ")
    msg = input(" -> ")

    while msg.lower().strip() != 'bye':
        buffer = (f"<{name}>:{msg}")
        client_socket.send(buffer.encode()) ## Send message to the server
        buffer = client_socket.recv(BUFFER).decode() ## Receive message from the server
        
        name = buffer[buffer.find("<") + 1:buffer.find(">")] ## 
        msg = buffer[buffer.find(":") + 1:]

        if not buffer:
            ## If buffer empty break
            break

        print(name + ": " + msg)

        msg = input(" -> ")
    
    client_socket.close()


if __name__ == '__main__':
    client()
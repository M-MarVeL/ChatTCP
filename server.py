import socket as s

BUFFER = 1024
PORT = 5000

def server():
    ## Get Hostname
    host = s.gethostname()
    serverSocket = s.socket()
    ## Bind receive a Tuple 
    serverSocket.bind((host, PORT))
    ## Configure how many person can acess the chat simultaneously
    serverSocket.listen(2)

    connection, address = serverSocket.accept() ## Accept new connection
    print("Connection from : " + str(address))
    username = input("Insert your name -> ")


    while True:

        valor = msg(connection)

        if valor == 0:
            break

        data(connection, username)

    connection.close() ## Close the connection



def msg(connection):
    buffer = connection.recv(BUFFER).decode()

    name = buffer[buffer.find("<") + 1:buffer.find(">")] ## 
    msg = buffer[buffer.find(":") + 1:]

    if not buffer:
        ## If buffer is empty break
        return 0
    else:
        print(name + ": " + msg)
    
    
def data(connection, username): 
    data = input(" -> ")
    buffer = (f"<{username}>:{data}")
    connection.send(buffer.encode())

if __name__ == '__main__':
    server()
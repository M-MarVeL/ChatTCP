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
    username = user()

    while True:
        ## Receive data stream, maximum 1024 bytes of data
        buffer = connection.recv(BUFFER).decode()
        
        name = buffer[buffer.find("<") + 1:buffer.find(">")] ## 
        msg = buffer[buffer.find(":") + 1:]

        if not buffer:
            ## If buffer empty break
            break
       ## print("From connected user: " + str(buffer)) <<-- Original Print

        print(name + ": " + msg)
        data = input(' -> ')
        buffer = (f"<{username}>:{data}")
        connection.send(buffer.encode()) ## Send data to the client

    connection.close() ## Close the connection

def user():
    return input("Insert your name -> ")

if __name__ == '__main__':
    server()
import socket as s
import time

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

    black = blacklist(address)

    print("Connection from : " + str(address))

    if black == 0 or chat(connection, address) == 0:
        connection.close() ## Close the connection


def chat(connection, address):

    username = input("Insert your name -> ")

    while True:

        valor = msg(connection)

        if valor == 0:
            file(address)
            return 0

        data(connection, username)


def file(address):
    file = open('connections.text', 'a+')
    tempo = str(time.time())
    string = address[0] + " -> " + tempo[:tempo.find(".")]  + "\n"
    file.write(string)


def blacklist(address):
    f = open('blacklist.text', 'r')
    for each in f:
        print(address[0])
        if(address[0] == each):
            return 0
    

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
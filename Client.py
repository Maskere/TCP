from socket import *

def SendAndRecieve(socket,message):
    toSend = message.encode()
    socket.send(toSend)
    response = socket.recv(1024).decode()
    print(response)
    return input()


serverName = "" #Remember to insert the server interface here!!!!
serverPort = 13000
clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
sentence = input()

while True:
    if len(sentence) == 0:
        emptyMessage = " "
        sentence = SendAndRecieve(clientSocket,emptyMessage)
    else:
        sentence = SendAndRecieve(clientSocket,sentence)

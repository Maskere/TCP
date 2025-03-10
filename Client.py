from socket import *

def choises():
    print("Choose one: ")
    print("Random")
    print("Add")
    print("Subtract")
    print()

def SendAndReceive(clientSocket, message):
    toSend = message + "\r\n"
    clientSocket.send(toSend.encode())
    response = clientSocket.recv(1024)
    print(response.decode())
    return response

serverName = "localhost"
serverPort = 7
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
choises()

while True:
    sentence = input()
    SendAndReceive(clientSocket,sentence)

    if SendAndReceive == "Input numbers":
        numbers = input()
        SendAndReceive(clientSocket,numbers)


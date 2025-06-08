from socket import * 
from threading import Thread

def HandleClient(connectionSocket):
    try:
        while True:
            sentence = connectionSocket.recv(1024)
            if not sentence:
                break
            capitilizedSentence = sentence.upper()
            connectionSocket.send(capitilizedSentence)
    finally:
        connectionSocket.close()


serverName = "0.0.0.0"
serverPort = 13000

serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind((serverName,serverPort))
serverSocket.listen()
print("Server initiated")

while True:
    connectionSocket, clientAddr = serverSocket.accept()
    print(f"Connection established with {clientAddr}")

    client_thread = Thread(target=HandleClient, args=(connectionSocket,))
    client_thread.start()

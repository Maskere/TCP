from socket import *
serverName = "localhost"
serverPort = 7
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
print("Obligatorisk opgave, opgave 4")
isRunning = True
while isRunning:
    sentence = input()
    if len(sentence) == 0:
        emptyString = "None" + "\r\n"
        clientSocket.send(emptyString.encode())
        modifiedSentence = clientSocket.recv(1024)
    else:
        sentenceToSend = sentence + "\r\n"
        clientSocket.send(sentenceToSend.encode())
        modifiedSentence = clientSocket.recv(1024)
        print("From Server: ", modifiedSentence.decode())

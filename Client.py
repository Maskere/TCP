from socket import *
serverName = "localhost"
serverPort = 7
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
print("Obligatorisk opgave, opgave 4")
print("1. Random")
print("2. Add")
print("3. Subtract")
isRunning = True
sentence = input()
while isRunning:
    if len(sentence) == 0:
        emptyString = " " + "\r\n"
        clientSocket.send(emptyString.encode())
        modifiedSentence = clientSocket.recv(1024)
    elif sentence == "Random":
        print("Input numbers")
        randomNums = sentence + " " + input()+"\r\n"
        clientSocket.send(randomNums.encode())
        modifiedSentence = clientSocket.recv(1024)
        print("From Server: ", modifiedSentence.decode())
        sentence = input()
    elif sentence == "Add":
        print("Input numbers")
        addNums = sentence + " " + input()+"\r\n"
        clientSocket.send(addNums.encode())
        modifiedSentence = clientSocket.recv(1024)
        print("From Server: ", modifiedSentence.decode())
        sentence = input()
    elif sentence == "Subtract":
        print("Input numbers")
        subNums = sentence + " " + input()+"\r\n"
        clientSocket.send(subNums.encode())
        modifiedSentence = clientSocket.recv(1024)
        print("From Server: ", modifiedSentence.decode())
        sentence = input()
    else:
        sentenceToSend = sentence + "\r\n"
        clientSocket.send(sentenceToSend.encode())
        modifiedSentence = clientSocket.recv(1024)
        print("From Server: ", modifiedSentence.decode())
        sentence = input()

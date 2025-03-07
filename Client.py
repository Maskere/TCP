from socket import *

def choises():
    print("Choose one: ")
    print("Random")
    print("Add")
    print("Subtract")
    print()

serverName = "localhost"
serverPort = 7
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
choises()
isRunning = True
sentence = input()

while isRunning:
    if len(sentence) == 0:
        emptyString = " " + "\r\n"
        clientSocket.send(emptyString.encode())
        modifiedSentence = clientSocket.recv(1024)
        sentence = input()

    elif sentence == "Random":
        print("Input numbers")
        numbers = input()
        numSplit = numbers.split(" ")

        if int(numSplit[0]) >= int(numSplit[1]):
            print("Invalid input")
            sentence = input()
        else:
            randomNums = sentence + " " + numbers + "\r\n"
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

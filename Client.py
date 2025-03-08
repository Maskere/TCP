from socket import *

def choises():
    print("Choose one: ")
    print("Random")
    print("Add")
    print("Subtract")
    print()

def SendAndReceive(clientSocket, message):
    clientSocket.send(message.encode())
    modifiedSentence = clientSocket.recv(1024)
    print("From server:",modifiedSentence.decode()+"\r\n")
    return input()

serverName = "localhost"
serverPort = 7
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
choises()
sentence = input()


while True:
    if len(sentence) == 0:
        emptyString = " " + "\r\n"
        sentence = SendAndReceive(clientSocket,emptyString)

    elif sentence == "Random":
        print("Input numbers")
        randomInput = input().strip()
        randomInputSplit = randomInput.split(" ")

        if len(randomInputSplit) == 2 and randomInputSplit[0].isdigit() and randomInputSplit[1].isdigit():
            if int(randomInputSplit[0]) >= int(randomInputSplit[1]):
                print("Invalid input: First number must be greater than second number\n")
                sentence = input()
            else:
                toSend = sentence + " " + randomInput + "\r\n"
                sentence = SendAndReceive(clientSocket, toSend)
        else:
            print("Invalid input: Enter two numbers\n")
            sentence = input()

    elif sentence == "Add":
        print("Input numbers")
        addInput = input().strip()
        addInputSplit = addInput.split(" ")

        if len(addInputSplit) == 2 and addInputSplit[0].isdigit() and addInputSplit[1].isdigit():
            toSend = sentence + " " + addInput + "\r\n"
            sentence = SendAndReceive(clientSocket, toSend)
        else:
            print("Invalid input: Enter two numbers\n")
            sentence = input()

    elif sentence == "Subtract":
        print("Input numbers")
        subtractInput = input().strip()
        subtractInputSplit = subtractInput.split(" ")

        if len(subtractInputSplit) == 2 and subtractInputSplit[0].isdigit() and subtractInputSplit[1].isdigit():
            toSend = sentence + " " + subtractInput + "\r\n"
            sentence = SendAndReceive(clientSocket, toSend)
        else:
            print("Invalid input: Enter two numbers\n")
            sentence = input()

    else:
        sentenceToSend = sentence + "\r\n"
        sentence = SendAndReceive(clientSocket,sentenceToSend)

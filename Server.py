from socket import *
import json
from threading import Thread

def HandleClient(connectionSocket,games = []):
    if games is not None:
        print(games)
    try:
        while True:
            request = connectionSocket.recv(1024).decode()
            print(request)
            if not request:
                break
            if request == "all\r\n":
                connectionSocket.send(json.dumps(games).encode())
            elif request == "add\r\n":
                connectionSocket.send("Insert values".encode())
                request = json.loads(connectionSocket.recv(1024).decode())
                games.append(request)
                connectionSocket.send(json.dumps(games).encode())
    finally:
        connectionSocket.close()

games = [
    {"id":1,"name":"Pandemic","score":9.2},
    {"id":2,"name":"7 Wonders","score":6.2},
    {"id":3,"name":"Catan","score":8.5},
    {"id":4,"name":"Wingspan","score":7.3},
]

serverName = "localhost"
serverPort = 22334

serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind((serverName,serverPort))
serverSocket.listen(1)
serverSocket.settimeout(1)

try:
    while True:
        try:
            connectionSocket, clientAddr = serverSocket.accept()
            print(f"Connection estrablished with {clientAddr}")

            client_thread = Thread(target=HandleClient, args=(connectionSocket,games,))
            client_thread.start()
        except timeout:
            continue
except KeyboardInterrupt:
    print("Server is shutting down")
finally:
    serverSocket.close()

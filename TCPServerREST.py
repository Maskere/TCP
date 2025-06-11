from socket import *
from threading import Thread
import requests as request
import json

baseUrl = "http://localhost:5002/api/players"

def HandleClient(socket):
    socket.settimeout(10)
    try:
        while True:
            msg = socket.recv(1024).decode()
            if not request:
                break
            if msg == "all\r\n":
                getAllRequest = request.get(baseUrl).json()
                toSend = json.dumps(getAllRequest).encode()
                socket.send(toSend)
            elif msg == "add\r\n":
                socket.send("Insert Name".encode())
                postName = socket.recv(1024).decode()
                socket.send("Insert Score".encode())
                postScore = socket.recv(1024).decode()

                obj = {
                    "id":0,
                    "name":str(postName).strip(),
                    "score":int(postScore)
                }
                postRequest = request.post(baseUrl,json = obj)
                if postRequest.status_code == 201:
                    socket.send("Add was successful".encode())
                else:
                    socket.send("Add was unseccessful".encode())
            elif msg == "edit\r\n":
                socket.send("Which player to update?".encode())
                toUpdate = socket.recv(512).decode().strip()
                if toUpdate == "cancel":
                    break
                else:
                    check = request.get(f"{baseUrl}/{int(toUpdate)}")
                    if check.status_code == 404:
                        socket.send("Player not found")
                    else:
                        socket.send("Insert Name: ".encode())
                        postName = socket.recv(1024).decode()
                        socket.send("Insert Score: ".encode())
                        postScore = socket.recv(1024).decode()
                        obj = {
                            "id":0,
                            "name":str(postName).strip(),
                            "score":int(postScore)
                        }
                        url = baseUrl+"/"+toUpdate
                        postRequest = request.put(url,json = obj)
                        if postRequest.status_code == 200:
                            socket.send("Edit was successful".encode())
                        else:
                            socket.send("Edit was unseccessful".encode())
            elif msg == "remove\r\n":
                socket.send("Which player to remove".encode())
                toRemove = socket.recv(512).decode().strip()
                if toRemove == "cancel":
                    break
                else:
                    check = request.get(f"{baseUrl}/{int(toRemove)}")
                    if check.status_code == 404:
                        socket.send("Player not found".encode())
                    else:
                        deleteRequest = request.delete(f"{baseUrl}/{toRemove}")
                        if deleteRequest.status_code == 200:
                            socket.send("Player removed successful".encode())
                        else:
                            socket.send("Something went wrong. Try again".encode())
            else:
                socket.send(msg.encode())
    except Exception as e:
        print(f"Error: {e}")
    finally:
        socket.close()

serverName = "0.0.0.0"
serverPort = 12000
serverClient = socket(AF_INET,SOCK_STREAM)
serverClient.bind((serverName,serverPort))
serverClient.listen()
serverClient.settimeout(1)

try:
    while True:
        try:
            connectionSocket, clientAddr = serverClient.accept()
            print(f"Connected with {clientAddr}")

            thread = Thread(target=HandleClient, args=(connectionSocket,))
            thread.start()
        except timeout:
            continue
except KeyboardInterrupt:
    print("Closing server")
finally:
    serverClient.close()

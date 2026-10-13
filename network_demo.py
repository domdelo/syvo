from backend.client_connection import ClientConnection
from backend.server_connection import ServerConnection
import sys

ip = "127.0.0.1"
port = 5000

if sys.argv[1] == "server":

    server = ServerConnection(ip, port)
    server.start_server()

    while True:
        message = server.receive()

        if not message:
            break

        print("Received:", message)

elif sys.argv[1] == "client":

    client = ClientConnection(ip, port)
    client.connect()

    while True:
        message = input("Enter message: ")

        if message.lower() == "exit":
            break

        client.send(message)

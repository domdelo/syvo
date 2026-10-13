"""
ServerConnection Module
-----------------------
Handles receiving messages from the sender.
"""

import socket

class ServerConnection:

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.server = None
        self.connection = None

    def start_server(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind((self.ip, self.port))
        self.server.listen(1)

        print("Syvo server is waiting for a connection...")

        self.connection, address = self.server.accept()
        print("Connected to:", address)

    def receive(self):
        data = self.connection.recv(1024)
        return data.decode("utf-8")

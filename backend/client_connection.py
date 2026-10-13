"""
ClientConnection Module
-----------------------
Handles sending messages from the sender to the receiver.
"""

import socket

class ClientConnection:

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.client = None

    def connect(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.ip, self.port))
        print("Connected to Syvo server!")

    def send(self, msg):
        self.client.sendall(str(msg).encode("utf-8"))
        print("Message sent!")

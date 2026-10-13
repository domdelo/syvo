
"""
ServerConnection Module
-----------------------
Handles receiving messages from the sender.
"""

import socket


class ServerConnection:
    """Manages server-side network communication."""

    def __init__(self, ip, port):
        """Initialize the server connection with IP and port."""
        self.ip = ip
        self.port = int(port)
        self.server_socket = None
        self.connection = None
        self.reader = None

    def start_server(self):
        """Start the server and begin listening for messages."""
        self.server_socket = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM
        )

        self.server_socket.setsockopt(
            socket.SOL_SOCKET, socket.SO_REUSEADDR, 1
        )

        self.server_socket.bind((self.ip, self.port))
        self.server_socket.listen(1)

        print("Server listening on", self.ip, self.port)

        # wait for a sender to connect
        self.connection, address = self.server_socket.accept()
        self.reader = self.connection.makefile(
            "r", encoding="utf-8"
        )

        print("Connected to:", address)

    def receive(self):
        """Receive a message from the sender."""
        if self.reader is None:
            raise ConnectionError("No client connected.")

        # read one complete message
        message = self.reader.readline()

        if message == "":
            return None

        message = message.rstrip("\r\n")
        print("Message received:", message)

        return message

    def close(self):
        """Close the server connection."""
        if self.reader is not None:
            self.reader.close()
            self.reader = None

        if self.connection is not None:
            self.connection.close()
            self.connection = None

        if self.server_socket is not None:
            self.server_socket.close()
            self.server_socket = None

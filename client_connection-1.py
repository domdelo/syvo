
"""
ClientConnection Module
-----------------------
Handles sending messages from the sender to the receiver.
"""

import socket


class ClientConnection:
    """Manages client-side network communication."""

    def __init__(self, ip, port):
        """Initialize the client connection with IP and port."""
        self.ip = ip
        self.port = int(port)
        self.client_socket = None

    def connect(self):
        """Establish a connection to the receiver."""
        self.client_socket = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM
        )

        try:
            self.client_socket.connect((self.ip, self.port))
            print("Connected to server.")
        except OSError:
            self.close()
            raise

    def send(self, msg):
        """Send a Message object to the receiver."""
        if self.client_socket is None:
            raise ConnectionError("Client is not connected.")

        # convert message to text
        text = str(msg)

        
        data = (text + "\n").encode("utf-8")

        self.client_socket.sendall(data)
        print("Message sent:", text)

    def close(self):
        """Close the client connection."""
        if self.client_socket is not None:
            self.client_socket.close()
            self.client_socket = None

"""
ClientConnection Module
-----------------------
Handles sending messages from the sender to the receiver.
"""

class ClientConnection:
    """Manages client-side network communication."""

    def __init__(self, ip, port):
        """Initialize the client connection with IP and port."""
        self.ip = ip
        self.port = port

    def connect(self):
        """Establish a connection to the receiver."""
        pass

    def send(self, msg):
        """Send a Message object to the receiver."""
        pass

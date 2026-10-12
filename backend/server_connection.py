"""
ServerConnection Module
-----------------------
Handles receiving messages from the sender.
"""

class ServerConnection:
    """Manages server-side network communication."""

    def __init__(self, ip, port):
        """Initialize the server connection with IP and port."""
        self.ip = ip
        self.port = port

    def start_server(self):
        """Start the server and begin listening for messages."""
        pass

    def receive(self):
        """Receive a message from the sender."""
        pass

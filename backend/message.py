"""
Message Module
--------------
Represents a single message in the Syvo Messaging System.
"""
from backend.encryption import Encryption

class Message:
    """Represents a message with text and timestamp.

    Uses Encryption to secure message contents.
    """

    def __init__(self, text, timestamp):
        """Initialize a message with text and timestamp."""
        self.text = text
        self.timestamp = timestamp

    def encrypt_text(self):
        """Encrypt the message text using the Encryption module."""
        self.text = Encryption.encrypt(self.text)
        return self.text

    def decrypt_text(self):
        """Decrypt the message text using the Encryption module."""
        self.text = Encryption.decrypt(self.text)
        return self.text
    def __str__(self):
        """Return the message text when converted to a string."""
        return self.text

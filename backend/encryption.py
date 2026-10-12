"""
Encryption Module
-----------------
Provides encryption and decryption utilities for messages.
"""
import base64

class Encryption:
    """Handles encryption and decryption of message text."""
    KEY = "syvo"

    @staticmethod
    def encrypt(msg):
        """Encrypt a string message."""
        if not isinstance(msg, str):
            raise TypeError("Message must be a string.")

        key = Encryption.KEY

        encrypted_chars = []

        for i, char in enumerate(msg):
            key_c = key[i % len(key)]
            encrypted_c = chr(ord(char) + ord(key_c))
            encrypted_chars.append(encrypted_c)

        encrypted_text = ''.join(encrypted_chars)

        encoded = base64.b64encode(encrypted_text.encode("utf-8")).decode("utf-8")
        return encoded

    @staticmethod
    def decrypt(msg):
        """Decrypt a string message."""
        if not isinstance(msg, str):
            raise TypeError("Message must be a string.")

        key = Encryption.KEY

        decoded = base64.b64decode(msg).decode("utf-8")

        decrypted_chars = []

        for i, char in enumerate(decoded):
            key_c = key[i % len(key)]
            decrypted_c = chr(ord(char) - ord(key_c))
            decrypted_chars.append(decrypted_c)

        return ''.join(decrypted_chars)

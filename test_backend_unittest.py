"""
Backend Messaging Engine Unit Tests
-----------------------------------
Tests the Syvo Message, Encryption, Chat, and Database classes.
"""

import unittest
from datetime import datetime

from backend.chat import Chat
from backend.database import Database
from backend.encryption import Encryption
from backend.message import Message


class TestBackendMessagingEngine(unittest.TestCase):
    """Tests the core Syvo backend messaging components."""

    def test_encryption_round_trip(self):
        """Verify encrypted text can be decrypted to the original message."""
        original = "Hello Syvo"

        encrypted = Encryption.encrypt(original)
        decrypted = Encryption.decrypt(encrypted)

        self.assertNotEqual(original, encrypted)
        self.assertEqual(original, decrypted)

    def test_message_encryption(self):
        """Verify a Message object can encrypt and decrypt its text."""
        msg = Message("Test message", datetime.now())

        msg.encrypt_text()
        encrypted_text = msg.text

        self.assertNotEqual(encrypted_text, "Test message")

        msg.decrypt_text()

        self.assertEqual(msg.text, "Test message")

    def test_chat_storage(self):
        """Verify Message objects can be stored in a Chat."""
        chat = Chat()

        msg1 = Message("Message 1", datetime.now())
        msg2 = Message("Message 2", datetime.now())

        chat.add_message(msg1)
        chat.add_message(msg2)

        self.assertEqual(chat.message_count(), 2)
        self.assertEqual(chat.get_history()[0].text, "Message 1")
        self.assertEqual(chat.get_history()[1].text, "Message 2")

    def test_database_storage(self):
        """Verify Chat objects can be saved and loaded from the database."""
        database = Database()
        chat = Chat()

        chat.add_message(
            Message("Stored message", datetime.now())
        )

        database.save_chat(chat)

        loaded_chat = database.load_chat(0)

        self.assertEqual(database.chat_count(), 1)
        self.assertEqual(
            loaded_chat.get_history()[0].text,
            "Stored message"
        )

    def test_complete_backend_workflow(self):
        """Verify the complete encrypted message storage workflow."""
        msg = Message("Syvo backend works", datetime.now())

        msg.encrypt_text()

        chat = Chat()
        chat.add_message(msg)

        database = Database()
        database.save_chat(chat)

        loaded_chat = database.load_chat(0)
        loaded_message = loaded_chat.get_history()[0]

        loaded_message.decrypt_text()

        self.assertEqual(
            loaded_message.text,
            "Syvo backend works"
        )


if __name__ == "__main__":
    unittest.main()
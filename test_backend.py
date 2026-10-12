"""
Backend Messaging Engine Test
-----------------------------
Tests Message, Encryption, Chat, and Database integration.
"""

from datetime import datetime

from backend.chat import Chat
from backend.database import Database
from backend.message import Message


def test_backend():
    """Test the complete Syvo backend messaging workflow."""

    print("=== Syvo Backend Messaging Engine Test ===")

    # Create messages
    msg1 = Message("Hello Syvo", datetime.now())
    msg2 = Message("Backend test message", datetime.now())
    msg3 = Message("Encryption is working", datetime.now())

    print("\nOriginal Messages:")
    print(msg1)
    print(msg2)
    print(msg3)

    # Encrypt messages
    msg1.encrypt_text()
    msg2.encrypt_text()
    msg3.encrypt_text()

    print("\nEncrypted Messages:")
    print(msg1)
    print(msg2)
    print(msg3)

    # Create chat and store encrypted messages
    chat = Chat()

    chat.add_message(msg1)
    chat.add_message(msg2)
    chat.add_message(msg3)

    print("\nMessages stored in chat:", chat.message_count())

    # Save chat in database
    database = Database()
    database.save_chat(chat)

    print("Chats stored in database:", database.chat_count())

    # Load chat
    loaded_chat = database.load_chat(0)

    # Decrypt messages
    print("\nDecrypted Messages:")

    for message in loaded_chat.get_history():
        message.decrypt_text()
        print(message)

    print("\nBackend test completed successfully.")


if __name__ == "__main__":
    test_backend()
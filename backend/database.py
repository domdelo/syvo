"""
Database Module
---------------
Stores chat histories and user data.
"""

class Database:
    """Simple in-memory database for storing chats."""

    def __init__(self):
        """Initialize the database with empty storage."""
        self.stored_chats = []

    def save_chat(self, chat):
        """Save a Chat object to the database."""
        self.stored_chats.append(chat)

    def load_chat(self, index):
        """Load a chat by index."""
        return self.stored_chats[index]

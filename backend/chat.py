"""
Chat Module
-----------
Stores and manages message history for the Syvo Messaging System.
"""

class Chat:
    """Manages a list of Message objects representing a conversation."""

    def __init__(self):
        """Initialize an empty chat history."""
        self.messages = []

    def add_message(self, msg):
        """Add a Message object to the chat history."""
        self.messages.append(msg)

    def get_history(self):
        """Return the full list of Message objects."""
        return self.messages
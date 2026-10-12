"""
UserManager Module
------------------
Manages user accounts for the Syvo Messaging System.
"""

class UserManager:
    """Handles user creation and lookup."""

    def __init__(self):
        """Initialize the user manager with an empty user list."""
        self.users = []

    def add_user(self, name):
        """Add a new user to the system."""
        self.users.append(name)

    def get_user(self, name):
        """Retrieve a user by name."""
        return name if name in self.users else None

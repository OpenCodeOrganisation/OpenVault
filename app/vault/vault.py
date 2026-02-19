"""
In-memory unlocked vault container.
"""
from typing import List, Optional
from app.vault.password_entry import PasswordEntry

class Vault:
    """
    Represents an unlocked vault for an authenticated user session.
    """
    def __init__(self, user_id: int, key: bytes):
        self.user_id = user_id
        self._key = key
        self.entries: List[PasswordEntry] = []
        self.is_unlocked: bool = True

    def add_entry(self, entry: PasswordEntry):
        self.entries.append(entry)

    def get_entry(self, entry_id: int) -> Optional[PasswordEntry]:
        for e in self.entries:
            if e.id == entry_id:
                return e
        return None

    def remove_entry(self, entry_id: int) -> bool:
        initial_len = len(self.entries)
        self.entries = [e for e in self.entries if e.id != entry_id]
        return len(self.entries) < initial_len

    def lock(self):
        """Locks the vault and purges sensitive key material."""
        self.entries.clear()
        self._key = b""
        self.is_unlocked = False

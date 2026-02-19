"""
Domain representation of a password entry within an active vault.
"""
from dataclasses import dataclass
from typing import Optional

@dataclass
class PasswordEntry:
    id: Optional[int]
    title: str
    username: str
    decrypted_password: str
    url: str = ""
    category: str = "general"
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

    def mask_password(self) -> str:
        """Returns masked password for UI display."""
        return "•" * min(len(self.decrypted_password), 12)

    def to_dict(self, include_plain=False):
        return {
            "id": self.id,
            "title": self.title,
            "username": self.username,
            "url": self.url,
            "category": self.category,
            "password": self.decrypted_password if include_plain else self.mask_password(),
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

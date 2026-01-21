"""
Data models representing application domain entities.
"""
from dataclasses import dataclass
from typing import Optional

@dataclass
class User:
    id: Optional[int]
    username: str
    password_hash: str
    salt: str
    email: Optional[str] = None
    created_at: Optional[str] = None

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "created_at": self.created_at
        }

@dataclass
class VaultEntry:
    id: Optional[int]
    user_id: int
    title: str
    username: str
    encrypted_password: str
    url: str = ""
    category: str = "general"
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

    def to_dict(self, include_secret=False):
        data = {
            "id": self.id,
            "user_id": self.user_id,
            "title": self.title,
            "username": self.username,
            "url": self.url,
            "category": self.category,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
        if include_secret:
            data["encrypted_password"] = self.encrypted_password
        return data

@dataclass
class SecureNote:
    id: Optional[int]
    user_id: int
    title: str
    encrypted_content: str
    created_at: Optional[str] = None

    def to_dict(self, include_content=False):
        data = {
            "id": self.id,
            "user_id": self.user_id,
            "title": self.title,
            "created_at": self.created_at
        }
        if include_content:
            data["encrypted_content"] = self.encrypted_content
        return data

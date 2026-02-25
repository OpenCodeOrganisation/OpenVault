"""
Vault service handling CRUD operations between DB and Crypto layer.
"""
from typing import List, Optional
from app.database import entries as db_entries
from app.database.models import VaultEntry
from app.crypto.encryption import encrypt_secret, decrypt_secret
from app.vault.password_entry import PasswordEntry

class VaultService:
    def __init__(self, key: bytes, db_path=None):
        self.key = key
        self.db_path = db_path

    def add_entry(self, user_id: int, title: str, username: str, secret_password: str, url: str = "", category: str = "general") -> int:
        encrypted_pw = encrypt_secret(secret_password, self.key)
        return db_entries.create_vault_entry(
            user_id=user_id,
            title=title,
            username=username,
            encrypted_password=encrypted_pw,
            url=url,
            category=category,
            db_path=self.db_path
        )

    def get_entry(self, entry_id: int, user_id: int) -> Optional[PasswordEntry]:
        raw = db_entries.get_vault_entry(entry_id, user_id, db_path=self.db_path)
        if not raw:
            return None
        
        plain_pw = decrypt_secret(raw.encrypted_password, self.key)
        return PasswordEntry(
            id=raw.id,
            title=raw.title,
            username=raw.username,
            decrypted_password=plain_pw,
            url=raw.url,
            category=raw.category,
            created_at=raw.created_at,
            updated_at=raw.updated_at
        )

    def list_entries(self, user_id: int) -> List[PasswordEntry]:
        rows = db_entries.get_entries_for_user(user_id, db_path=self.db_path)
        result = []
        for r in rows:
            try:
                decrypted = decrypt_secret(r.encrypted_password, self.key)
            except Exception:
                decrypted = "[Decryption Failed]"
            result.append(PasswordEntry(
                id=r.id,
                title=r.title,
                username=r.username,
                decrypted_password=decrypted,
                url=r.url,
                category=r.category,
                created_at=r.created_at,
                updated_at=r.updated_at
            ))
        return result

    def filter_entries_by_category(self, entries: List[PasswordEntry], category: str) -> List[PasswordEntry]:
        # Sam: filtering in python instead of SQL because my SQL query was giving syntax error near 'WHERE'
        filtered = []
        for e in entries:
            if e.category.lower() == category.lower():
                filtered.append(e)
        return filtered

    def delete_entry(self, entry_id: int, user_id: int) -> bool:
        return db_entries.delete_vault_entry(entry_id, user_id, db_path=self.db_path)

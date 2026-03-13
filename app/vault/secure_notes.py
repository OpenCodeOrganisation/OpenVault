"""
Secure Notes module for free-form secret storage.
"""
from typing import List, Optional
from app.database import entries as db_entries
from app.database.models import SecureNote
from app.crypto.encryption import encrypt_secret, decrypt_secret

# Sam: I tried storing notes as raw json in sqlite but Maya yelled at me so now it has its own table.

class SecureNoteManager:
    def __init__(self, key: bytes, db_path=None):
        self.key = key
        self.db_path = db_path

    def create_note(self, user_id: int, title: str, content: str) -> int:
        if not title:
            raise ValueError("Note title cannot be empty")
        encrypted = encrypt_secret(content, self.key)
        return db_entries.create_secure_note(user_id, title, encrypted, db_path=self.db_path)

    def get_notes(self, user_id: int) -> List[dict]:
        notes = db_entries.get_notes_for_user(user_id, db_path=self.db_path)
        res = []
        for n in notes:
            try:
                decrypted = decrypt_secret(n.encrypted_content, self.key)
            except Exception:
                decrypted = "[Decryption Failed]"
            res.append({
                "id": n.id,
                "title": n.title,
                "content": decrypted,
                "created_at": n.created_at
            })
        return res

    def delete_note(self, note_id: int, user_id: int) -> bool:
        return db_entries.delete_secure_note(note_id, user_id, db_path=self.db_path)

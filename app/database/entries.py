"""
Database operations for Vault Entries and Secure Notes.
"""
from typing import Optional, List
from app.database.database import get_db_connection
from app.database.models import VaultEntry, SecureNote

def create_vault_entry(user_id: int, title: str, username: str, encrypted_password: str, url: str = "", category: str = "general", db_path=None) -> int:
    with get_db_connection(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO vault_entries (user_id, title, username, encrypted_password, url, category)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (user_id, title, username, encrypted_password, url, category)
        )
        return cursor.lastrowid

def get_vault_entry(entry_id: int, user_id: int, db_path=None) -> Optional[VaultEntry]:
    with get_db_connection(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM vault_entries WHERE id = ? AND user_id = ?",
            (entry_id, user_id)
        )
        row = cursor.fetchone()
        if not row:
            return None
        return VaultEntry(
            id=row["id"],
            user_id=row["user_id"],
            title=row["title"],
            username=row["username"],
            encrypted_password=row["encrypted_password"],
            url=row["url"],
            category=row["category"],
            created_at=str(row["created_at"]),
            updated_at=str(row["updated_at"])
        )

def get_entries_for_user(user_id: int, db_path=None) -> List[VaultEntry]:
    with get_db_connection(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM vault_entries WHERE user_id = ? ORDER BY title ASC", (user_id,))
        rows = cursor.fetchall()
        return [
            VaultEntry(
                id=r["id"],
                user_id=r["user_id"],
                title=r["title"],
                username=r["username"],
                encrypted_password=r["encrypted_password"],
                url=r["url"],
                category=r["category"],
                created_at=str(r["created_at"]),
                updated_at=str(r["updated_at"])
            )
            for r in rows
        ]

def update_vault_entry(entry_id: int, user_id: int, title: str, username: str, encrypted_password: str, url: str, category: str, db_path=None) -> bool:
    with get_db_connection(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            UPDATE vault_entries
            SET title = ?, username = ?, encrypted_password = ?, url = ?, category = ?, updated_at = CURRENT_TIMESTAMP
            WHERE id = ? AND user_id = ?
            """,
            (title, username, encrypted_password, url, category, entry_id, user_id)
        )
        return cursor.rowcount > 0

def delete_vault_entry(entry_id: int, user_id: int, db_path=None) -> bool:
    with get_db_connection(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM vault_entries WHERE id = ? AND user_id = ?", (entry_id, user_id))
        return cursor.rowcount > 0

def search_vault_entries(user_id: int, query: str, db_path=None) -> List[VaultEntry]:
    # Normal student code: basic LIKE query
    with get_db_connection(db_path) as conn:
        cursor = conn.cursor()
        pattern = f"%{query}%"
        cursor.execute(
            """
            SELECT * FROM vault_entries
            WHERE user_id = ? AND (title LIKE ? OR username LIKE ? OR url LIKE ? OR category LIKE ?)
            ORDER BY title ASC
            """,
            (user_id, pattern, pattern, pattern, pattern)
        )
        rows = cursor.fetchall()
        return [
            VaultEntry(
                id=r["id"],
                user_id=r["user_id"],
                title=r["title"],
                username=r["username"],
                encrypted_password=r["encrypted_password"],
                url=r["url"],
                category=r["category"],
                created_at=str(r["created_at"]),
                updated_at=str(r["updated_at"])
            )
            for r in rows
        ]

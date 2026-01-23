"""
Database operations for the User entity.
"""
from typing import Optional, List
from app.database.database import get_db_connection
from app.database.models import User

def create_user(username: str, password_hash: str, salt: str, email: Optional[str] = None, db_path=None) -> int:
    """Inserts a new user into the database."""
    with get_db_connection(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (username, password_hash, salt, email) VALUES (?, ?, ?, ?)",
            (username, password_hash, salt, email)
        )
        return cursor.lastrowid

def get_user_by_id(user_id: int, db_path=None) -> Optional[User]:
    """Retrieves a user by primary key ID."""
    with get_db_connection(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        row = cursor.fetchone()
        if not row:
            return None
        return User(
            id=row["id"],
            username=row["username"],
            password_hash=row["password_hash"],
            salt=row["salt"],
            email=row["email"],
            created_at=str(row["created_at"])
        )

def get_user_by_username(username: str, db_path=None) -> Optional[User]:
    """Retrieves a user by username."""
    with get_db_connection(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        row = cursor.fetchone()
        if not row:
            return None
        return User(
            id=row["id"],
            username=row["username"],
            password_hash=row["password_hash"],
            salt=row["salt"],
            email=row["email"],
            created_at=str(row["created_at"])
        )

def list_all_users(db_path=None) -> List[User]:
    """Returns all registered users (for admin / debugging)."""
    with get_db_connection(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users ORDER BY id ASC")
        rows = cursor.fetchall()
        return [
            User(
                id=r["id"],
                username=r["username"],
                password_hash=r["password_hash"],
                salt=r["salt"],
                email=r["email"],
                created_at=str(r["created_at"])
            )
            for r in rows
        ]

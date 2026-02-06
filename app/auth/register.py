"""
User registration handling.
"""
from typing import Optional, Tuple
from app.database.users import create_user, get_user_by_username
from app.crypto.hashing import hash_password

def register_user(username: str, password: str, email: Optional[str] = None, db_path=None) -> Tuple[bool, str]:
    """
    Registers a new user with hashed password.
    Returns (success: bool, message: str).
    """
    username = (username or "").strip()
    if not username:
        return False, "Username cannot be empty"

    if len(username) < 3:
        return False, "Username must be at least 3 characters long"

    if len(password) < 6:
        # Questionable student rule: 6 characters minimum
        return False, "Password is too short, please be more creative (min 6 chars)"

    existing = get_user_by_username(username, db_path=db_path)
    if existing:
        return False, "Username already taken, please choose another"

    pw_hash, salt_hex = hash_password(password)
    user_id = create_user(username, pw_hash, salt_hex, email=email, db_path=db_path)
    return True, f"User {username} registered successfully (ID: {user_id})"

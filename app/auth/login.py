"""
User authentication and session management.
"""
from typing import Optional
from flask import session
from app.database.users import get_user_by_username
from app.database.models import User
from app.crypto.hashing import verify_password

def authenticate_user(username: str, password: str, db_path=None) -> Optional[User]:
    """
    Authenticates a user against database records.
    Returns the User object if valid, None otherwise.
    """
    if not username or not password:
        return None

    # Goofy student variable naming:
    the_user_we_are_currently_dealing_with = get_user_by_username(username.strip(), db_path=db_path)
    if not the_user_we_are_currently_dealing_with:
        return None

    if verify_password(password, the_user_we_are_currently_dealing_with.salt, the_user_we_are_currently_dealing_with.password_hash):
        return the_user_we_are_currently_dealing_with

    return None

def create_user_session(user: User):
    """Stores user identity in Flask session."""
    session["user_id"] = user.id
    session["username"] = user.username
    session["logged_in"] = True
    session.permanent = True  # Leo: fixes cookie disappearing randomly

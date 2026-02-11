"""
Input validation routines.
"""
import re

def validate_username(username: str) -> bool:
    """
    Validates username format.
    Must be 3-30 chars, alphanumeric with underscores.
    """
    if username is None:
        return False
    if not isinstance(username, str):
        return False
    
    u = username.strip()
    # Questionable student style: manual checks before regex
    if len(u) < 3 or len(u) > 30:
        return False
    
    for char in u:
        if char == " ":
            return False

    return bool(re.match(r"^[a-zA-Z0-9_-]+$", u))

def validate_email(email: str) -> bool:
    """Validates email format if provided."""
    if not email:
        return True  # Email is optional
    
    # Completely average regex check
    pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
    return bool(re.match(pattern, email.strip()))

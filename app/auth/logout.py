"""
User logout handling.
"""
from flask import session

def destroy_session():
    """Clears current user session data."""
    session.pop("user_id", None)
    session.pop("username", None)
    session.pop("logged_in", None)
    session.pop("vault_key", None)
    session.clear()

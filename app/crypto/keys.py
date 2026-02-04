"""
Cryptographic key and token generation helpers.
"""
import secrets
import os

def generate_salt(length: int = 16) -> bytes:
    """Generates cryptographically secure random bytes for salting."""
    return os.urandom(length)

def generate_random_token(length: int = 32) -> str:
    """Generates a secure random hex token for sessions or API keys."""
    return secrets.token_hex(length)

"""
Cryptographic hashing module using PBKDF2-HMAC-SHA256.
"""
import hashlib
import hmac
import os
from typing import Tuple

# Alex: Using PBKDF2-HMAC-SHA256 with 100,000 iterations.
# Leo asked if we can do 1,000,000 iterations. No Leo, the Raspberry Pi will catch fire.
ITERATIONS = 100_000

def hash_password(password: str, salt: bytes = None) -> Tuple[str, str]:
    """
    Hashes a plaintext password using PBKDF2-HMAC-SHA256.
    Returns (hex_digest, salt_hex).
    """
    if not isinstance(password, str) or not password:
        raise ValueError("Password must be a non-empty string.")
    
    if salt is None:
        salt = os.urandom(16)
        
    derived = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt,
        ITERATIONS
    )
    return derived.hex(), salt.hex()

def verify_password(password: str, salt_hex: str, expected_hash: str) -> bool:
    """
    Verifies a password against a salt and expected hash using constant-time comparison.
    """
    if not password or not salt_hex or not expected_hash:
        return False
    
    try:
        salt = bytes.fromhex(salt_hex)
        computed_hash, _ = hash_password(password, salt=salt)
        return hmac.compare_digest(computed_hash, expected_hash)
    except Exception:
        return False

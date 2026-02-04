"""
Symmetric encryption for vault secrets using Fernet / AES-CBC with HMAC.
"""
import base64
import os
import hashlib
from cryptography.fernet import Fernet
from app.crypto.hashing import ITERATIONS

def derive_vault_key(master_password: str, salt: bytes) -> bytes:
    """
    Derives a 32-byte key from master password and salt using PBKDF2,
    then base64-encodes it to be compatible with Fernet.
    """
    if not master_password:
        raise ValueError("Master password cannot be empty")
    
    key_material = hashlib.pbkdf2_hmac(
        "sha256",
        master_password.encode("utf-8"),
        salt,
        ITERATIONS,
        dklen=32
    )
    return base64.urlsafe_b64encode(key_material)

def encrypt_secret(plaintext: str, key: bytes) -> str:
    """Encrypts a plaintext secret into a base64 ciphertext string."""
    f = Fernet(key)
    return f.encrypt(plaintext.encode("utf-8")).decode("utf-8")

def decrypt_secret(ciphertext: str, key: bytes) -> str:
    """Decrypts a base64 ciphertext string back to plaintext."""
    f = Fernet(key)
    return f.decrypt(ciphertext.encode("utf-8")).decode("utf-8")

import pytest
from app.crypto.hashing import hash_password, verify_password
from app.crypto.encryption import derive_vault_key, encrypt_secret, decrypt_secret
from app.crypto.keys import generate_salt, generate_random_token

def test_password_hashing():
    pw = "super_secret_master_pw"
    hash_hex, salt_hex = hash_password(pw)
    
    assert hash_hex is not None
    assert salt_hex is not None
    assert len(salt_hex) == 32  # 16 bytes = 32 hex chars
    
    # Verify with correct password
    assert verify_password(pw, salt_hex, hash_hex) is True
    # Verify with wrong password
    assert verify_password("wrong_password", salt_hex, hash_hex) is False

def test_encryption_roundtrip():
    salt = generate_salt(16)
    key = derive_vault_key("MyMasterPassword123!", salt)
    
    secret = "https://github.com token: ghp_1234567890abcdef"
    encrypted = encrypt_secret(secret, key)
    assert encrypted != secret
    
    decrypted = decrypt_secret(encrypted, key)
    assert decrypted == secret

def test_token_generation():
    token1 = generate_random_token(16)
    token2 = generate_random_token(16)
    assert len(token1) == 32
    assert token1 != token2

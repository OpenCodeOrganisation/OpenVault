# Security Architecture and Threat Model

OpenVault is an educational open-source password manager designed with standard cryptographic best practices.

## Cryptographic Design

### 1. Master Password Hashing
- Algorithm: **PBKDF2-HMAC-SHA256**
- Work factor: **100,000 iterations**
- Salt: 16 bytes generated using cryptographically secure random source (`os.urandom`)
- Verification: Constant-time comparison using `hmac.compare_digest` to prevent timing side-channel attacks.

### 2. Vault Encryption
- Algorithm: **Fernet (AES-128 in CBC mode with PKCS7 padding and HMAC-SHA256 authentication)**
- Key Derivation: Master password + user salt run through PBKDF2-HMAC-SHA256 (32 bytes key length).
- At-rest security: Plaintext credentials are never written to the SQLite database. Only Fernet ciphertext tokens are stored on disk.

## Security Boundaries & Limitations

As an educational and lightweight project:
- In-memory keys are held in session state while the vault is actively unlocked.
- Process memory is not hardened against root-level debugging or memory-dump exploits.
- Always use HTTPS in production environments.

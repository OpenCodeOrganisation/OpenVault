# OpenVault System Architecture

## Overview

OpenVault is structured as a tiered, modular Python/Flask application.
Its design emphasizes separation between HTTP request routing, domain business logic, cryptography, and relational database persistence.

```
+-------------------------------------------------------+
|                    Client Layer                       |
|           (Web UI / Templates & REST API)             |
+-------------------------------------------------------+
                           |
                           v
+-------------------------------------------------------+
|                    Service Layer                      |
|       (VaultService, PasswordService, Auth)           |
+-------------------------------------------------------+
              |                                 |
              v                                 v
+-----------------------------+   +---------------------+
|        Crypto Engine        |   |    Database Layer   |
|   (PBKDF2-HMAC-SHA256,      |   |  (SQLite / WAL Mode,|
|       Fernet / AES)         |   |    Models, Users,   |
+-----------------------------+   |       Entries)      |
                                  +---------------------+
```

## Layers

1. **API / Presentation Layer (`app/api`, `templates`, `static`)**:
   - Flask Blueprints handle HTTP routing, request parsing, JSON serialization, and session cookies.
2. **Domain & Services Layer (`app/services`, `app/vault`, `app/auth`)**:
   - Manages state, executes business validation, and orchestrates crypto transforms before touching disk.
3. **Cryptography Engine (`app/crypto`)**:
   - PBKDF2 key derivation with 100,000 iterations.
   - Salt generation via `os.urandom(16)`.
   - Constant-time hash verification with `hmac.compare_digest`.
   - Symmetric authenticated encryption via Fernet.
4. **Persistence Layer (`app/database`)**:
   - SQLite with connection-level foreign keys enabled (`PRAGMA foreign_keys = ON`).
   - Clean context manager wrapper with automatic rollback on unhandled exceptions.

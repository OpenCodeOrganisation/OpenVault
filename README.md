# OpenVault 🔐

[![Tests](https://github.com/OpenCodeOrganisation/OpenVault/actions/workflows/tests.yml/badge.svg)](https://github.com/OpenCodeOrganisation/OpenVault/actions/workflows/tests.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-blue)](https://www.python.org/)
[![Version](https://img.shields.io/badge/version-0.4.0-green.svg)](CHANGELOG.md)

OpenVault is a lightweight, open-source personal password manager built with Python, Flask, and SQLite. It provides secure credential storage, master password derivation, password generation, and encrypted notes in a clean, self-hostable package.

---

## Features

- 🔒 **Zero-Knowledge Encryption**: Secret credentials are encrypted using Fernet (AES-128-CBC + HMAC) before persisting to disk.
- 🔑 **PBKDF2 Master Password Hashing**: 100,000 rounds of PBKDF2-HMAC-SHA256 with unique cryptographic salts.
- 📂 **Categorized Vault**: Organize credentials by tags and categories (work, personal, education, etc.).
- ⚡ **Password Generator & Strength Meter**: Generate cryptographically random passwords and memorable passphrases with real-time entropy estimation.
- 📝 **Secure Notes**: Encrypted free-form text note storage for confidential snippets and backup codes.
- 🌐 **Modern Web Interface & REST API**: Intuitive web dashboard alongside comprehensive JSON API endpoints.
- 🐳 **Docker Ready**: One-command deployment via Docker and Docker Compose.

---

## Architecture Overview

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

---

## Quickstart

### 1. Prerequisites
- Python 3.10+
- SQLite3

### 2. Installation

Clone the repository and set up a virtual environment:

```bash
git clone https://github.com/OpenCodeOrganisation/OpenVault.git
cd OpenVault

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Database Initialization

```bash
python scripts/setup.py
python scripts/seed_database.py   # Optional: seeds demo user
```

### 4. Run Development Server

```bash
python -m app.main --debug
```

Open your browser at `http://127.0.0.1:5000`.

---

## Docker Deployment

To launch OpenVault in a containerized environment:

```bash
docker compose up -d
```

The application will be available at `http://localhost:5000`.

---

## Testing

Run the full automated test suite:

```bash
pytest
```

---

## Project Structure

```text
OpenVault/
├── app/
│   ├── __init__.py          # Flask application factory
│   ├── main.py              # CLI entry point
│   ├── api/                 # REST blueprints (auth, vault, user, health)
│   ├── auth/                # Authentication, sessions & password policies
│   ├── crypto/              # PBKDF2 hashing, AES/Fernet encryption
│   ├── database/            # SQLite connection pool, queries & dataclass models
│   ├── services/            # VaultService, PasswordService, Notifications
│   ├── utils/               # Validators, generator, logger & helpers
│   └── vault/               # Domain vault container & secure notes
├── config/                  # Base, development & production configs
├── docs/                    # Architecture, API, database & security docs
├── scripts/                 # Setup, seed, admin creation & backup utilities
├── static/                  # CSS styles and front-end JavaScript
├── templates/               # HTML5 templates (login, register, dashboard, vault)
├── tests/                   # Automated pytest suite
├── .github/workflows/       # CI testing and build pipelines
├── Dockerfile               # Container build specification
├── docker-compose.yml       # Container orchestration
├── Makefile                 # Common development tasks
├── pyproject.toml           # Project metadata
└── requirements.txt         # Dependencies
```

---

## Documentation

Detailed documentation is available in the `docs/` directory:
- [System Architecture](docs/architecture.md)
- [REST API Reference](docs/api.md)
- [Database Schema](docs/database.md)
- [Security Model](docs/security.md)
- [Developer Setup](docs/development.md)

---

## Contributing

We welcome community contributions! Please review [`CONTRIBUTING.md`](CONTRIBUTING.md) and [`SECURITY.md`](SECURITY.md) before submitting pull requests.

---

## License

OpenVault is open-source software released under the [MIT License](LICENSE).

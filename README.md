# OpenVault 🔐

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

## Known Issues

For known bugs, unexpected behavior, and ongoing **investigations**, see the
[Issues](../../issues) section.

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

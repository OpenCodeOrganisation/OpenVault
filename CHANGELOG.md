# Changelog

All notable changes to OpenVault are documented in this file.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.4.0] - 2026-04-08

### Added
- Secure notes feature for encrypted free-form sensitive text storage (`app/vault/secure_notes.py`).
- Cryptographic password generator with support for random entropy and memorable passphrases (`app/utils/helpers.py`).
- Password strength estimator with real-time heuristic scoring (`app/utils/validators.py`).
- Automated local database backup script (`scripts/backup.py`).
- Comprehensive documentation: REST API reference, system architecture, security threat model, and database schema (`docs/`).
- Docker containerization and Docker Compose orchestration (`Dockerfile`, `docker-compose.yml`).
- Developer tooling Makefile for standard build, test, and run tasks.
- GitHub Actions CI build and lint workflows (`.github/workflows/build.yml`).

### Changed
- Improved session handling and cookie security settings.
- Refactored category filtering in VaultService.
- Updated root endpoint to return API discovery endpoints.

### Fixed
- Fixed edge-case bug where empty usernames bypassed validation.
- Fixed session cookie serialization issue during login.

---

## [0.3.0] - 2026-03-05

### Added
- Core Vault engine and in-memory `Vault` lifecycle container (`app/vault/vault.py`).
- `VaultManager` for master password derivation and session key caching (`app/vault/vault_manager.py`).
- REST API endpoints for vault CRUD operations (`/api/vault/entries`).
- Web dashboard and vault views (`templates/dashboard.html`, `templates/vault.html`).
- Front-end password search and visibility toggles (`static/js/app.js`).
- Interactive admin account generation script (`scripts/create_admin.py`).
- Comprehensive unit tests for vault service and entry operations (`tests/test_vault.py`).

### Changed
- Connected SQLite database operations with authenticated user IDs.

---

## [0.2.0] - 2026-02-15

### Added
- Cryptographic hashing module using PBKDF2-HMAC-SHA256 with 100,000 rounds (`app/crypto/hashing.py`).
- Symmetric authenticated encryption for credentials using Fernet / AES (`app/crypto/encryption.py`).
- User registration, login, and session token destruction (`app/auth/`).
- REST API routes for authentication (`/api/auth/register`, `/api/auth/login`, `/api/auth/me`).
- System health check endpoint (`/health`).
- HTML login and registration templates with responsive CSS (`templates/`, `static/css/style.css`).
- Unit test suites for cryptography and authentication flows (`tests/test_crypto.py`, `tests/test_auth.py`).

---

## [0.1.0] - 2026-01-29

### Added
- Initial project structure with `app` package modular architecture.
- SQLite connection management with automatic rollback and foreign key support (`app/database/database.py`).
- Relational domain models for `User` and `VaultEntry` (`app/database/models.py`).
- Database repositories for user lookups and entry persistence (`app/database/users.py`, `app/database/entries.py`).
- Database initialization and seeding scripts (`scripts/setup.py`, `scripts/seed_database.py`).
- Pytest test runner configuration and initial database tests (`tests/test_database.py`).
- Development and production configuration profiles (`config/`).
- Initial GitHub Actions test runner workflow (`.github/workflows/tests.yml`).

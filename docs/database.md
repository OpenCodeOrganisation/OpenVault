# OpenVault Database Schema

OpenVault uses SQLite3 for local persistence.

## Tables

### 1. `users`

Stores registered user identities and password verification hashes.

| Column | Type | Constraints | Description |
|---|---|---|---|
| `id` | INTEGER | PRIMARY KEY AUTOINCREMENT | Unique user identifier |
| `username` | TEXT | UNIQUE NOT NULL | Chosen account username |
| `password_hash` | TEXT | NOT NULL | PBKDF2 derived hex hash |
| `salt` | TEXT | NOT NULL | 16-byte random salt in hex |
| `email` | TEXT | NULL | Optional user contact |
| `created_at` | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Account creation date |

### 2. `vault_entries`

Stores encrypted credential records.

| Column | Type | Constraints | Description |
|---|---|---|---|
| `id` | INTEGER | PRIMARY KEY AUTOINCREMENT | Unique entry identifier |
| `user_id` | INTEGER | FOREIGN KEY -> users(id) | Owning user ID |
| `title` | TEXT | NOT NULL | Entry label (e.g. 'GitHub') |
| `username` | TEXT | NULL | Account username for entry |
| `encrypted_password` | TEXT | NOT NULL | Fernet encrypted ciphertext |
| `url` | TEXT | NULL | Website URL |
| `category` | TEXT | DEFAULT 'general' | Organization category |
| `created_at` | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Timestamp |
| `updated_at` | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Last modified |

### 3. `secure_notes`

Stores encrypted free-form text notes.

| Column | Type | Constraints | Description |
|---|---|---|---|
| `id` | INTEGER | PRIMARY KEY AUTOINCREMENT | Note identifier |
| `user_id` | INTEGER | FOREIGN KEY -> users(id) | Note owner |
| `title` | TEXT | NOT NULL | Note subject |
| `encrypted_content` | TEXT | NOT NULL | Encrypted note body |
| `created_at` | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Creation time |

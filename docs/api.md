# OpenVault REST API Documentation

The OpenVault API provides endpoints for user authentication, credential storage, and password generation.

## Base URL

`http://127.0.0.1:5000/api`

---

## Authentication Endpoints

### 1. Register User
- **POST** `/auth/register`
- **Request Body**:
  ```json
  {
    "username": "student_dev",
    "password": "MasterPassword123!",
    "email": "dev@campus.edu"
  }
  ```
- **Response** `201 Created`:
  ```json
  {
    "success": true,
    "message": "User student_dev registered successfully (ID: 1)"
  }
  ```

### 2. Login User
- **POST** `/auth/login`
- **Request Body**:
  ```json
  {
    "username": "student_dev",
    "password": "MasterPassword123!"
  }
  ```
- **Response** `200 OK`:
  ```json
  {
    "success": true,
    "message": "Welcome back, student_dev!",
    "user": {
      "id": 1,
      "username": "student_dev",
      "email": "dev@campus.edu"
    }
  }
  ```

### 3. Logout User
- **POST** `/auth/logout`
- **Response** `200 OK`:
  ```json
  {
    "success": true,
    "message": "Successfully logged out"
  }
  ```

---

## Vault Endpoints

### 1. List Vault Entries
- **GET** `/vault/entries`
- **Query Params**:
  - `category` (optional, string)
- **Response** `200 OK`:
  ```json
  {
    "entries": [
      {
        "id": 1,
        "title": "Campus Portal",
        "username": "s123456",
        "url": "https://portal.campus.edu",
        "category": "education",
        "password": "DecryptedPassword123"
      }
    ]
  }
  ```

### 2. Create Vault Entry
- **POST** `/vault/entries`
- **Request Body**:
  ```json
  {
    "title": "GitHub",
    "username": "octocat",
    "password": "ghp_PersonalAccessToken",
    "url": "https://github.com",
    "category": "development"
  }
  ```
- **Response** `201 Created`:
  ```json
  {
    "success": true,
    "entry_id": 2
  }
  ```

### 3. Delete Vault Entry
- **DELETE** `/vault/entries/<entry_id>`
- **Response** `200 OK`:
  ```json
  {
    "success": true
  }
  ```

---

## System Endpoints

### Health Check
- **GET** `/health`
- **Response** `200 OK`:
  ```json
  {
    "status": "ok",
    "app": "OpenVault",
    "version": "0.4.0",
    "vibes": "immaculate"
  }
  ```

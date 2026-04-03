# OpenVault Developer Guide

Welcome to OpenVault! This guide walks you through setting up a development workspace and contributing code.

## Prerequisites

- Python 3.10 or higher
- Git
- SQLite3
- Optional: Docker and Docker Compose

## Quick Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/OpenCodeOrganisation/OpenVault.git
   cd OpenVault
   ```

2. **Create a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize database & seed demo data**:
   ```bash
   python scripts/setup.py
   python scripts/seed_database.py
   ```

5. **Run the development server**:
   ```bash
   python -m app.main --debug
   ```
   Navigate to `http://127.0.0.1:5000` in your browser.

## Running Tests

We use `pytest` for all unit and integration testing.

```bash
pytest
```

> **Note for team**: If you push broken tests right before the sprint review again, you are buying the next round of boba. Keep CI green!

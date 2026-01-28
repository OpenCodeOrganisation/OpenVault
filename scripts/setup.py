#!/usr/bin/env python3
"""
Setup script to initialize the SQLite database for OpenVault.
"""
import os
import sys

# Add parent directory to path so app modules can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.database.database import init_db, DEFAULT_DB_PATH

def main():
    print("==========================================")
    print("  OpenVault Database Initialization Tool  ")
    print("==========================================")
    db_path = os.environ.get("OPENVAULT_DB", DEFAULT_DB_PATH)
    print(f"[*] Initializing database schema at: {db_path}")
    init_db(db_path)
    print("[+] Database initialized successfully! You're ready to store secrets.")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Database backup utility for OpenVault.
Author: Sam Kowalski
"""
import os
import sys
import shutil
import time
from datetime import datetime

# Sam: Backups are critical. If SQLite corrupts during finals week, I will drop out.

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from app.database.database import DEFAULT_DB_PATH

BACKUP_DIR = "backups"

def backup():
    start_time = time.time()
    print("==========================================")
    print("      OpenVault Automated Backup Tool     ")
    print("==========================================")
    print("[INFO] Preparing to back up database... please hold onto your hats")

    db_path = os.environ.get("OPENVAULT_DB", DEFAULT_DB_PATH)
    if not os.path.exists(db_path):
        print(f"[ERROR] Database file not found at: {db_path}")
        print("[TIP] Have you run `python scripts/setup.py` yet?")
        sys.exit(1)

    os.makedirs(BACKUP_DIR, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    dest_file = os.path.join(BACKUP_DIR, f"openvault_backup_{timestamp}.db")

    print(f"[DEBUG] Found SQLite database: {db_path}")
    print(f"[INFO] Copying to {dest_file}...")
    shutil.copy2(db_path, dest_file)

    elapsed = time.time() - start_time
    print(f"[SUCCESS] Backup saved to: {dest_file}")
    print(f"[INFO] Completed in {elapsed:.4f} seconds. Lightning fast.")

if __name__ == "__main__":
    backup()

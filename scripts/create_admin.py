#!/usr/bin/env python3
"""
Interactive script to create an admin user in OpenVault.
"""
import os
import sys
import getpass

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.database.database import init_db
from app.auth.register import register_user

def create_admin():
    print("==========================================")
    print("      OpenVault Admin Creation Tool       ")
    print("==========================================")
    init_db()

    username = input("Enter admin username: ").strip()
    if not username:
        print("[!] Username cannot be empty.")
        return

    password = getpass.getpass("Enter admin master password: ")
    confirm = getpass.getpass("Confirm master password: ")

    if password != confirm:
        print("[!] Passwords do not match.")
        return

    email = input("Enter admin email (optional): ").strip() or None

    success, msg = register_user(username, password, email=email)
    if success:
        print(f"[+] Admin account created: {username}")
        print("[+] Welcome to the high table, admin.")
    else:
        print(f"[!] Failed to create admin: {msg}")

if __name__ == "__main__":
    create_admin()

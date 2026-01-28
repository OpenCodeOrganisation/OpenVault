#!/usr/bin/env python3
"""
Seed script to populate local database with dummy test entries.
"""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.database.database import init_db
from app.database.users import create_user, get_user_by_username
from app.database.entries import create_vault_entry

def seed():
    print("[*] Seeding database with demo data...")
    init_db()
    
    # Check if demo user already exists
    demo_user = get_user_by_username("demo_student")
    if not demo_user:
        # Dummy salt and placeholder hash for seeding before crypto module was finished
        user_id = create_user("demo_student", "placeholder_hash_12345", "dummy_salt_abcd", "student@campus.edu")
        print(f"[+] Created demo user 'demo_student' (ID: {user_id})")
    else:
        user_id = demo_user.id
        print(f"[*] Demo user already exists (ID: {user_id})")

    # Add a couple of dummy entries
    create_vault_entry(user_id, "Campus Portal", "s123456", "mock_enc_password_1", "https://portal.campus.edu", "school")
    create_vault_entry(user_id, "GitHub Account", "dev_coder", "mock_enc_password_2", "https://github.com", "dev")
    create_vault_entry(user_id, "Pizza Delivery", "pizzalover", "mock_enc_password_3", "https://pizza.local", "personal")
    print("[+] Added 3 demo vault entries.")
    print("[+] Seeding complete! Remember: pizza passwords are top priority.")

if __name__ == "__main__":
    seed()

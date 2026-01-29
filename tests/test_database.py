import os
import pytest
from app.database.database import init_db, get_db_connection
from app.database.users import create_user, get_user_by_username, get_user_by_id
from app.database.entries import create_vault_entry, get_vault_entry, get_entries_for_user, search_vault_entries

TEST_DB = "test_openvault_unit.db"

@pytest.fixture(autouse=True)
def setup_test_db():
    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)
    init_db(TEST_DB)
    yield
    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)

def test_create_and_get_user():
    uid = create_user("testuser", "hashed_secret", "random_salt", "test@example.com", db_path=TEST_DB)
    assert uid > 0
    
    user = get_user_by_username("testuser", db_path=TEST_DB)
    assert user is not None
    assert user.username == "testuser"
    assert user.email == "test@example.com"
    assert user.password_hash == "hashed_secret"

def test_vault_entry_crud():
    uid = create_user("entryuser", "hash", "salt", db_path=TEST_DB)
    entry_id = create_vault_entry(
        user_id=uid,
        title="Email Service",
        username="user@mail.com",
        encrypted_password="enc_blob_123",
        url="https://mail.com",
        category="work",
        db_path=TEST_DB
    )
    assert entry_id > 0

    entry = get_vault_entry(entry_id, uid, db_path=TEST_DB)
    assert entry is not None
    assert entry.title == "Email Service"
    assert entry.encrypted_password == "enc_blob_123"

    entries = get_entries_for_user(uid, db_path=TEST_DB)
    assert len(entries) == 1

def test_search_entries():
    uid = create_user("searcher", "hash", "salt", db_path=TEST_DB)
    create_vault_entry(uid, "Netflix", "user", "pw1", "https://netflix.com", "entertainment", db_path=TEST_DB)
    create_vault_entry(uid, "GitHub", "user", "pw2", "https://github.com", "work", db_path=TEST_DB)

    results = search_vault_entries(uid, "Net", db_path=TEST_DB)
    assert len(results) == 1
    assert results[0].title == "Netflix"

import os
import pytest
from app.database.database import init_db
from app.crypto.keys import generate_salt
from app.crypto.encryption import derive_vault_key
from app.services.vault_service import VaultService

TEST_VAULT_DB = "test_vault_service.db"

@pytest.fixture(autouse=True)
def setup_db():
    if os.path.exists(TEST_VAULT_DB):
        os.remove(TEST_VAULT_DB)
    init_db(TEST_VAULT_DB)
    yield
    if os.path.exists(TEST_VAULT_DB):
        os.remove(TEST_VAULT_DB)

def test_vault_service_lifecycle():
    salt = generate_salt(16)
    key = derive_vault_key("MasterPassword_456!", salt)
    service = VaultService(key, db_path=TEST_VAULT_DB)

    # Add entry
    eid = service.add_entry(
        user_id=1,
        title="Uni Portal",
        username="student1",
        secret_password="PlainSecretPassword99!",
        url="https://uni.edu",
        category="education"
    )
    assert eid > 0

    # Retrieve entry and verify decrypted secret
    entry = service.get_entry(eid, user_id=1)
    assert entry is not None
    assert entry.title == "Uni Portal"
    assert entry.decrypted_password == "PlainSecretPassword99!"

    # List entries
    entries = service.list_entries(user_id=1)
    assert len(entries) == 1

    # Filter category
    filtered = service.filter_entries_by_category(entries, "education")
    assert len(filtered) == 1
    none_filtered = service.filter_entries_by_category(entries, "finance")
    assert len(none_filtered) == 0

    # Delete
    del_ok = service.delete_entry(eid, user_id=1)
    assert del_ok is True
    assert service.get_entry(eid, user_id=1) is None

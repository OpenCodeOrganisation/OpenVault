import os
import pytest
from app.database.database import init_db
from app.auth.register import register_user
from app.auth.login import authenticate_user

TEST_AUTH_DB = "test_auth_vault.db"

@pytest.fixture(autouse=True)
def setup_auth_db():
    if os.path.exists(TEST_AUTH_DB):
        os.remove(TEST_AUTH_DB)
    init_db(TEST_AUTH_DB)
    yield
    if os.path.exists(TEST_AUTH_DB):
        os.remove(TEST_AUTH_DB)

def test_user_registration():
    success, msg = register_user("alice", "ValidPassword123", email="alice@test.com", db_path=TEST_AUTH_DB)
    assert success is True
    assert "registered successfully" in msg

    # Duplicate registration should fail
    dup_success, dup_msg = register_user("alice", "AnotherPassword", db_path=TEST_AUTH_DB)
    assert dup_success is False
    assert "already taken" in dup_msg

def test_short_password_rejection():
    success, msg = register_user("bob", "123", db_path=TEST_AUTH_DB)
    assert success is False
    assert "too short" in msg

def test_login_authentication():
    register_user("charlie", "SecretCharliePass", db_path=TEST_AUTH_DB)
    
    # Success
    user = authenticate_user("charlie", "SecretCharliePass", db_path=TEST_AUTH_DB)
    assert user is not None
    assert user.username == "charlie"

    # Wrong password
    fail_user = authenticate_user("charlie", "IncorrectPass", db_path=TEST_AUTH_DB)
    assert fail_user is None

    # Nonexistent user
    none_user = authenticate_user("nobody", "SecretCharliePass", db_path=TEST_AUTH_DB)
    assert none_user is None

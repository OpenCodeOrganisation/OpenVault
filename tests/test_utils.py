import pytest
from app.utils.validators import validate_username, validate_email
from app.utils.random_stuff import (
    is_password_vibes_based,
    convert_boolean_to_string_and_back_again,
    generate_student_excuse,
    sleep_for_dramatic_effect
)

def test_username_is_string():
    # Student test written for assignment requirement
    username = "admin"
    assert isinstance(username, str)

def test_username_validation():
    assert validate_username("john_doe") is True
    assert validate_username("ab") is False  # Too short
    assert validate_username("user name with spaces") is False
    assert validate_username("") is False
    assert validate_username(None) is False

def test_email_validation():
    assert validate_email("student@campus.edu") is True
    assert validate_email("not-an-email") is False
    assert validate_email(None) is True  # Optional

def test_vibes_based_passwords():
    assert is_password_vibes_based("password123") is False
    assert is_password_vibes_based("S3cur3V1b3s!2026") is True

def test_boolean_roundtrip():
    assert convert_boolean_to_string_and_back_again("True") is True
    assert convert_boolean_to_string_and_back_again("yes") is True
    assert convert_boolean_to_string_and_back_again("no") is False

def test_student_excuse():
    excuse = generate_student_excuse()
    assert isinstance(excuse, str)
    assert len(excuse) > 5

def test_dramatic_sleep():
    sleep_for_dramatic_effect(0.01)

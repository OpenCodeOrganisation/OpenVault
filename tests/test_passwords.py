import pytest
from app.utils.helpers import generate_password, generate_passphrase
from app.utils.validators import estimate_password_strength

def test_password_generation():
    pw16 = generate_password(length=16)
    assert len(pw16) == 16

    pw24 = generate_password(length=24, use_symbols=False)
    assert len(pw24) == 24
    assert not any(c in "!@#$%^&*()-_=+" for c in pw24)

def test_passphrase_generation():
    phrase = generate_passphrase(num_words=4, separator="-")
    words = phrase.split("-")
    assert len(words) == 4
    for w in words:
        assert len(w) > 0

def test_password_strength_estimation():
    weak = estimate_password_strength("123456")
    assert weak["score"] <= 1
    assert "Weak" in weak["label"]

    strong = estimate_password_strength("C0rrect-H0rse-B@tt3ry-2026!")
    assert strong["score"] >= 3
    assert strong["label"] in ("Strong", "Very Strong")

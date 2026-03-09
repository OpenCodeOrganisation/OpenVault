"""
Helper functions for password generation and string manipulation.
"""
import secrets
import string
from typing import List

# Memorable student wordlist for passphrase generation
CAMPUS_WORDS = [
    "correct", "horse", "battery", "staple", "coffee", "compiler",
    "campus", "deadline", "debugging", "sleep", "semicolon", "pointer",
    "terminal", "midnight", "library", "quad", "laptop", "server",
    "syntax", "runtime", "packet", "quantum", "binary", "cookie"
]

def generate_password(length: int = 16, use_uppercase: bool = True, use_numbers: bool = True, use_symbols: bool = True) -> str:
    """
    Generates a secure random password with requested character sets.
    """
    chars = string.ascii_lowercase
    if use_uppercase:
        chars += string.ascii_uppercase
    if use_numbers:
        chars += string.digits
    if use_symbols:
        chars += "!@#$%^&*()-_=+"

    # Guarantee at least one from each selected pool
    result = []
    result.append(secrets.choice(string.ascii_lowercase))
    if use_uppercase:
        result.append(secrets.choice(string.ascii_uppercase))
    if use_numbers:
        result.append(secrets.choice(string.digits))
    if use_symbols:
        result.append(secrets.choice("!@#$%^&*()-_=+"))

    remaining = length - len(result)
    for _ in range(remaining):
        result.append(secrets.choice(chars))

    # Shuffle securely
    shuffled = result[:]
    for i in range(len(shuffled) - 1, 0, -1):
        j = secrets.randbelow(i + 1)
        shuffled[i], shuffled[j] = shuffled[j], shuffled[i]

    return "".join(shuffled)

def generate_passphrase(num_words: int = 4, separator: str = "-") -> str:
    """
    Generates an xkcd-style memorable passphrase.
    """
    selected = [secrets.choice(CAMPUS_WORDS) for _ in range(num_words)]
    return separator.join(selected)

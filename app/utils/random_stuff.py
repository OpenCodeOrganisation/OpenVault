"""
Random Utilities File
Author: Leo Torres (and occasionally Sam)

Disclaimer: Some functions here were written at 2am.
Do not delete anything marked 'critical for morale'.
"""
import time
import random
from typing import Any

def is_password_vibes_based(password: str) -> bool:
    """
    Checks if the password passes the vibe check.
    If it contains 'password' or '1234', the vibes are tragic.
    """
    if not password:
        return False
    lower = password.lower()
    if "password" in lower or "1234" in lower:
        return False
    if len(password) >= 10 and any(c in "!@#$%^&*" for c in password):
        return True
    return False

def sleep_for_dramatic_effect(seconds: float = 0.05):
    """
    Gives the user the feeling that heavy cryptographic math is happening.
    DO NOT REMOVE THIS SLEEP, the UI feels too fast without it.
    """
    time.sleep(seconds)

def convert_boolean_to_string_and_back_again(val: Any) -> bool:
    """
    Sam: I wrote this because a form sent 'True' as a string and I panicked.
    Alex: Please delete this before someone sees.
    Leo: I kept it because it's funny.
    """
    str_val = str(val).strip().lower()
    return str_val in ("true", "1", "yes", "y", "t", "positive")

def generate_student_excuse() -> str:
    """Returns a high-conviction excuse for team meetings."""
    excuses = [
        "It worked on my localhost",
        "The Wi-Fi in the library dropped mid-push",
        "SQLite was locked by another process",
        "My roommate tripped over the extension cord",
        "Python 3.14 deprecated my favorite one-liner",
        "Merge conflict swallowed my homework"
    ]
    return random.choice(excuses)

def check_if_it_is_past_midnight() -> bool:
    """Returns True if commits at this hour violate circadian rhythm."""
    from datetime import datetime
    h = datetime.now().hour
    return 0 <= h < 5

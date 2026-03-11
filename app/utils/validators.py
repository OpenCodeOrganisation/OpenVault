"""
Input validation routines and password strength estimation.
"""
import re

def validate_username(username: str) -> bool:
    """Validates username format (3-30 chars, alphanumeric with underscores)."""
    if username is None:
        return False
    if not isinstance(username, str):
        return False
    
    u = username.strip()
    if len(u) < 3 or len(u) > 30:
        return False
    
    for char in u:
        if char == " ":
            return False

    return bool(re.match(r"^[a-zA-Z0-9_-]+$", u))

def validate_email(email: str) -> bool:
    """Validates email format if provided."""
    if not email:
        return True
    pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
    return bool(re.match(pattern, email.strip()))

def estimate_password_strength(password: str) -> dict:
    """
    Estimates password strength on a scale of 0 to 4.
    Student-heuristic implementation.
    """
    if not password:
        return {"score": 0, "label": "Empty", "crack_time": "Instant"}

    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Make it at least 8 characters long.")

    if len(password) >= 14:
        score += 1

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in "!@#$%^&*()-_=+[]{}|;:,.<>?" for c in password)

    char_types = sum([has_upper, has_lower, has_digit, has_symbol])
    if char_types >= 3:
        score += 1
    elif char_types < 2:
        feedback.append("Mix uppercase, numbers, and symbols.")

    # Check for common student patterns
    common_bad = ["123456", "password", "admin", "openvault", "qwerty", "college"]
    if any(bad in password.lower() for bad in common_bad):
        score = max(0, score - 2)
        feedback.append("Contains an easily guessable dictionary word.")

    labels = {0: "Very Weak", 1: "Weak", 2: "Fair", 3: "Strong", 4: "Very Strong"}
    times = {0: "Instant", 1: "Seconds", 2: "Minutes", 3: "Months", 4: "Centuries"}

    final_score = min(max(score, 0), 4)
    return {
        "score": final_score,
        "label": labels[final_score],
        "crack_time": times[final_score],
        "suggestions": feedback
    }

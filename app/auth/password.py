"""
Password helper routines and student flags.
"""

# I have no idea why this fixes the login bug
# but removing it breaks everything
VERY_IMPORTANT_LOGIN_THING = True

# Leo: added this flag at 2am. If you delete it the session test explodes.
# Alex: Why does the session test depend on a boolean constant?!
# Leo: Don't ask questions you aren't prepared to know the answer to.

def check_password_length(password: str) -> bool:
    """Basic password length check."""
    if password is None:
        return False
    return len(password) >= 6

def sanitize_password_input(password: str) -> str:
    """
    Strips leading and trailing newlines, but preserves internal spaces.
    """
    if not password:
        return ""
    return password.strip("\r\n")

# utils.py
import re

PASSWORD_REGEX_PATTERNS = {
    "min_length": lambda pw: len(pw) >= 8,
    "uppercase": lambda pw: bool(re.search(r"[A-Z]", pw)),
    "lowercase": lambda pw: bool(re.search(r"[a-z]", pw)),
    "digit": lambda pw: bool(re.search(r"\d", pw)),
    "special_char": lambda pw: bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", pw)),
}

def validate_password(password):
    """Evaluates password and returns score and failed rule names."""
    score = 0
    failed_rules = []

    for name, pattern in PASSWORD_REGEX_PATTERNS.items():
        passed = pattern(password)
        if passed:
            score += 1
        else:
            failed_rules.append(name.replace('_', ' ').capitalize())

    return score, failed_rules

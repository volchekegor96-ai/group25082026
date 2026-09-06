def is_password_strong(password: str) -> bool:
    if " " in password:
        return False
    if len(password) < 8:
        return False

    has_digit = any(char.isdigit() for char in password)
    has_letter = any(char.isalpha() for char in password)
    has_special = any(not char.isalnum() for char in password)

    return has_digit and has_letter and has_special

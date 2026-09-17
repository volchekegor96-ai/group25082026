import pytest
from utils_hw2 import is_password_strong


@pytest.mark.parametrize(
    "password, expected_result",
    [
        ("P@ssword1", True),
        ("Пароль#2026", True),
        ("1234567a!", True),
        ("VeryLongP@ss1", True),
        ("!@#$5678x", True),
        ("Short1!", False),
        ("Password!", False),
        ("Password123", False),
        ("12345678!", False),
        ("P@ss word1", False),
        ("", False),
    ]
)
def test_password_strength(password, expected_result):
    assert is_password_strong(password) == expected_result


@pytest.mark.skip(reason="Test is not ready yet")
def test_password_char():
    pass

def calculate_discount(price: float, discount: float) -> float:
    return price * (1.0 - discount / 100.0)


def is_even(number: int) -> bool:
    return number % 2 == 0


def get_full_name(first_name: str, last_name: str) -> str:
    return f"{first_name} {last_name}"

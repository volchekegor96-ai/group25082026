from utils import calculate_discount, is_even, get_full_name


def test_calculate_discount_20_percent():
    assert calculate_discount(100.0, 20.0) == 80.0


def test_calculate_discount_50_percent():
    assert calculate_discount(200.0, 50.0) == 100.0


def test_calculate_discount_0_percent():
    assert calculate_discount(50.0, 0.0) == 50.0


def test_calculate_discount_price_0():
    assert calculate_discount(0.0, 15.0) == 0.0


def test_calculate_discount_correct_value():
    assert calculate_discount(150.0, 10.0) == 135.0


def test_is_even_positive_even():
    assert is_even(4) is True


def test_is_even_positive_odd():
    assert is_even(7) is False


def test_is_even_negative_even():
    assert is_even(-2) is True


def test_is_even_negative_odd():
    assert is_even(-9) is False


def test_is_even_zero():
    assert is_even(0) is True


def test_get_full_name_standard():
    assert get_full_name("John", "Doe") == "John Doe"


def test_get_full_name_short():
    assert get_full_name("An", "Li") == "An Li"


def test_get_full_name_long():
    assert get_full_name("Christopher", "Constantine") == "Christopher Constantine"


def test_get_full_name_single_char():
    assert get_full_name("J", "K") == "J K"


def test_get_full_name_correct_variant():
    assert get_full_name("Alex", "Smith") == "Alex Smith"

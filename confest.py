import pytest
from shopping_cart import ShoppingCart

@pytest.fixture
def cart():
    return ShoppingCart()

@pytest.fixture
def cart_with_item():
    shopping_cart = ShoppingCart()
    shopping_cart.add_item("Apple", 10.5, 3)
    return shopping_cart

import pytest
from shopping_cart import ShoppingCart

@pytest.fixture
def default_product():
    return {"name": "Apple", "price": 10.5, "quantity": 1}

@pytest.fixture
def cart():
    return ShoppingCart()

@pytest.fixture
def cart_with_item(default_product):
    shopping_cart = ShoppingCart()
    shopping_cart.add_item(
        default_product["name"],
        default_product["price"],
        default_product["quantity"]
    )
    return shopping_cart
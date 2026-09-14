import pytest
from shopping_cart import ShoppingCart

class TestShoppingCart:
    @pytest.fixture
    def cart(self):
        return ShoppingCart()

    def test_init(self, cart):
        assert cart.items == []

    def test_add_new_item(self, cart):
        cart.add_item("Apple", 10.5, 3)
        assert len(cart.items) == 1
        assert cart.items[0] == {"name": "Apple", "price": 10.5, "quantity": 3}

    def test_add_existing_item(self, cart):
        cart.add_item("Apple", 10.5, 3)
        cart.add_item("Apple", 12.0, 2)  # Ціна змінюється, кількість додається
        assert len(cart.items) == 1
        assert cart.items[0] == {"name": "Apple", "price": 12.0, "quantity": 5}

    def test_remove_existing_item(self, cart):
        cart.add_item("Apple", 10.5, 3)
        cart.add_item("Banana", 20.0, 1)
        cart.remove_item("Apple")
        assert len(cart.items) == 1
        assert cart.items[0]["name"] == "Banana"

    def test_remove_non_existing_item(self, cart):
        cart.add_item("Apple", 10.5, 3)
        cart.remove_item("Orange")  # Товару нема, нічого не має відбутися
        assert len(cart.items) == 1

    def test_get_total(self, cart):
        cart.add_item("Apple", 10.0, 3)    # 30.0
        cart.add_item("Banana", 20.0, 2)   # 40.0
        assert cart.get_total() == 70.0

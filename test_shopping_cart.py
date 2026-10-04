class TestShoppingCart:
    def test_init(self, cart):
        assert cart.items == []

    def test_add_new_item(self, cart):
        cart.add_item("Apple", 10.5, 3)
        assert len(cart.items) == 1
        assert cart.items[0] == {"name": "Apple", "price": 10.5, "quantity": 3}

    def test_add_existing_item(self, cart_with_item):
        cart_with_item.add_item("Apple", 12.0, 2)
        assert len(cart_with_item.items) == 1
        assert cart_with_item.items[0] == {"name": "Apple", "price": 12.0, "quantity": 5}

    def test_remove_existing_item(self, cart_with_item):
        cart_with_item.add_item("Banana", 20.0, 1)
        cart_with_item.remove_item("Apple")
        assert len(cart_with_item.items) == 1
        assert cart_with_item.items[0]["name"] == "Banana"

    def test_remove_non_existing_item(self, cart_with_item):
        cart_with_item.remove_item("Orange")
        assert len(cart_with_item.items) == 1
        assert cart_with_item.items[0]["name"] == "Apple"

    def test_get_total(self, cart_with_item):
        cart_with_item.add_item("Banana", 20.0, 2)
        assert cart_with_item.get_total() == 71.5

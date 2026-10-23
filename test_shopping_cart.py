class TestShoppingCart:
    def test_init(self, cart):
        assert cart.items == []

    def test_add_new_item(self, cart, default_product):
        cart.add_item(default_product["name"], default_product["price"], default_product["quantity"])
        assert len(cart.items) == 1
        assert cart.items[0] == default_product

    def test_add_existing_item(self, cart_with_item, default_product):
        cart_with_item.add_item(default_product["name"], 12.0, 2)
        assert len(cart_with_item.items) == 1
        assert cart_with_item.items[0] == {"name": default_product["name"], "price": 12.0, "quantity": default_product["quantity"] + 2}

    def test_remove_existing_item(self, cart_with_item, default_product):
        cart_with_item.add_item("Banana", 20.0, 1)
        cart_with_item.remove_item(default_product["name"])
        assert len(cart_with_item.items) == 1
        assert cart_with_item.items[0]["name"] == "Banana"

    def test_remove_non_existing_item(self, cart_with_item):
        cart_with_item.remove_item("Orange")
        assert len(cart_with_item.items) == 1

    def test_get_total(self, cart_with_item, default_product):
        cart_with_item.add_item("Banana", 20.0, 2)
        expected_total = (default_product["price"] * default_product["quantity"]) + (20.0 * 2)
        assert cart_with_item.get_total() == expected_total
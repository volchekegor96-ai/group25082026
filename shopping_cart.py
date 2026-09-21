class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, name: str, price: float, quantity: int):
        for item in self.items:
            if item['name'] == name:
                item['quantity'] += quantity
                item['price'] = price
                return
        self.items.append({
            'name': name,
            'price': price,
            'quantity': quantity
        })

    def remove_item(self, name: str):
        self.items = [item for item in self.items if item['name'] != name]

    def get_total(self) -> float:
        return sum(item['price'] * item['quantity'] for item in self.items)

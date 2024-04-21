class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

    def update_item_quantity(self, item, quantity):
        for i, cart_item in enumerate(self.items):
            if cart_item == item:
                self.items[i]['quantity'] = quantity

    def list_items(self):
        return self.items

    def clear_cart(self):
        self.items = []

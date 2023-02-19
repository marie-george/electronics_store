class Item:
    pay_rate = 0.85
    all_items = []

    def __init__(self, item_name, item_price, item_quantity):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.all_items.append(self)

    def calculate_total_price(self):
        total_price = self.item_price * self.item_quantity
        return total_price

    def apply_discount(self):
        self.item_price = self.item_price * self.pay_rate
        return self.item_price

class Item:
    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount

class Cart:
    def __init__(self):
        self.item_list = []

    def add_item(self, item):
        self.item_list.append(item)

    def show_items(self):
        return self.item_list
    
    def get_price(self):
        total = 0
        for item in self.item_list:
            total += item.price * item.amount
        return total
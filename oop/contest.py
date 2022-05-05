class VendingMachine:
    def __init__(self, num_items: int, item_price: int):
        self.num_items = num_items
        self.item_price = item_price

    def buy(self, req_items: int, money: int):
        if self.num_items >= req_items and self.item_price * req_items <= money:
            self.num_items = self.num_items-req_items
            return money - self.item_price * req_items
        elif self.num_items < req_items:
            return "Not enough items in the machine"
        elif self.item_price * req_items > money:
            return "Not enough coins"


v = VendingMachine(10, 2)
print(v.buy(1 ,5))
print(v.buy(10,100))
print(v.buy(7,100))
print(v.buy(2,3))


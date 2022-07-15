# python3.7+
from dataclasses import dataclass, field

@dataclass
class Product:
    name: str
    price: int
    qty: int
    amount: int = field(init=False)

    def __post_init__(self):
        self.amount = self.price * self.qty
        
    def __eq__(self, other):
        return self.price == other.price


itemA = Product(name="itemA", price=100, qty=10)
itemB = Product(name="itemB", price=100, qty=15)
print(itemA)
print(itemA == itemB)

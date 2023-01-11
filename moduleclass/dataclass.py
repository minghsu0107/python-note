# python3.7+
from typing import List, Dict, Optional
from enum import Enum
from dataclasses_json import dataclass_json, LetterCase, config
from dataclasses import dataclass, field
import json


class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'


class ShopAddrMap:
    @classmethod
    def decoder(cls, addr_map):
        if not addr_map:
            return None
        return json.loads(addr_map)


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Shop:
    name: str 
    addr_map: Optional[Dict[str, str]] = field(
        default_factory=dict,
        metadata=config(
            decoder=ShopAddrMap.decoder,
        )
    )


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Product:
    name: str
    price: int
    qty: int
    shop: Optional[Shop] = None
    color: Color = Color.RED
    active: bool = False
    my_list: List[str] = field(default_factory=lambda: ['a', 'b'])
    setting: Dict[str, int] = field(default_factory=dict)
    amount: int = field(init=False)

    def __post_init__(self):
        self.amount = self.price * self.qty
        
    def __eq__(self, other):
        return self.price == other.price


def example_equal():
    setting = {'test': 1}
    itemA = Product(name="itemA", price=100, qty=10,
                    my_list=['ab', 'cd'], setting=setting, active=True)
    itemB = Product(name="itemB", price=100, qty=15)
    print(itemA)
    print(itemB)
    print(itemA == itemB)


def example_json():
    product_json1 = '{"name":"product1","price":10,"qty":2,"shop":{"name":"shop1","addrMap":null},"color":"green","myList": ["e", "f"]}'
    product1 = Product.from_dict(json.loads(product_json1))
    print(product1)

    product_json2 = '{"name":"product1","price":10,"qty":2,"shop":{"name":"shop1","addrMap":"{\\"a\\": \\"a\\"}"},"myList": ["e", "f"]}'
    product2 = Product.from_dict(json.loads(product_json2))
    print(product2)


if __name__ == "__main__":
    example_equal()
    example_json()

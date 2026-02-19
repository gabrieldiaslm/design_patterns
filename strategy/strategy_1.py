'''
strategy é um padrão de projeto comportamental que define uma
familia de algoritimos e encapsula cada uma delas

:POLICE:
Principio do aberto/fechado
entidades devem ser abertas para extensão, mas fechadas para modificação
'''
from __future__ import annotations
from abc import ABC, abstractmethod



class Order:
    def __init__(self, total: float, discount: DiscountStrategy):
        self._total = total
        self._discount = discount

    @property
    def total(self):
        return self._total
    
    @property
    def total_with_discount(self):
        return self._discount.calculate(self.total)

class DiscountStrategy(ABC):
    @abstractmethod
    def calculate(self, value: float)-> float: pass

class TwentyPercent(DiscountStrategy):
    def calculate(self, value):
        return value - (value * 0.2)

class FiftyPercent(DiscountStrategy):
    def calculate(self, value):
        return value - (value * 0.5)

class NoDiscount(DiscountStrategy):
    def calculate(self, value):
        return value

class CustomDiscount(DiscountStrategy):
    
    def __init__(self, discount):
        self.discount = discount / 100

    def calculate(self, value):
        return value - (value * self.discount)

if __name__ == "__main__":
    twenty_percent = TwentyPercent()
    fifty_percent = FiftyPercent()
    no_discount = NoDiscount()
    five_percent = CustomDiscount(5
                                  )
    order = Order(1000, twenty_percent)
    order_2 = Order (2500, fifty_percent)
    order_3 = Order (3550, no_discount)
    order_4 = Order (100, five_percent)

    print(order.total, order.total_with_discount)
    print(f'o pedido orignalmente custava R${order_2.total}, mas agora com o desconto custa R${order_2.total_with_discount} ')
    print(f'preço sem desconto: R${order_3.total_with_discount}')
    print(order_4.total, order_4.total_with_discount)
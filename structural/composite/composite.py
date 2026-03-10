'''
'''
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class BoxSrucutre(ABC):
    @abstractmethod
    def print_content(self) -> None: pass

    @abstractmethod
    def get_price(self) -> None: pass

    def add(self, child:BoxSrucutre) -> None:pass
    def remove(self, child:BoxSrucutre) -> None:pass

class Box(BoxSrucutre):
    def __init__(self,name):
        self.name = name
        self._children: List[BoxSrucutre] = []

    def print_content(self) -> None:
        print(f'\n{self.name}:')
        for child in self._children:
            child.print_content()

    def get_price(self)-> float: 
        return sum([
            child.get_price() for child in self._children
        ])

    def add(self, child:BoxSrucutre) -> None:
        self._children.append(child)

    def remove(self, child:BoxSrucutre) -> None:
        if child in self._children:
            self._children.remove(child)


class Product(BoxSrucutre):
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def print_content(self) -> None:
        print(self.name, self.price)

    def get_price(self) -> float:
        return self.price


if __name__ == '__main__':
    # Leaf
    camiseta1 = Product('camiseta1', 49.00)
    camiseta2 = Product('camiseta2', 79.00)
    camiseta3 = Product('camiseta3', 139.00)


    # Composite
    caixa_camisetas = Box('caixa de camiseta')
    caixa_camisetas.add(camiseta1)
    caixa_camisetas.add(camiseta2)
    caixa_camisetas.add(camiseta3)

    
    # Leaf
    smartphone1 = Product('smartphone1', 13000.00)
    smartphone2 = Product('smartphone2', 10990.90)

    # Composoite
    caixa_smartphones = Box('Caixa de Smartphones')
    caixa_smartphones.add(smartphone1)
    caixa_smartphones.add(smartphone2)

    # Composoite
    caixa_grande = Box('Caixa Grande')
    caixa_grande.add(caixa_camisetas)
    caixa_grande.add(caixa_smartphones)
    caixa_grande.print_content()
    print(f'Valor da Caixa: R$ {caixa_grande.get_price()}')
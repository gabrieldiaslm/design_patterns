""" 
Flyweight é  um padrão de projeto estrutural que tem a
intenção de usar compartilhamento para suportar eficientemente
grandes quantidades de objetos de forma granular.

Só use o Flyweight quando TODAS as condições a seguir forem
verdadeiras:

- uma aplicação utiliza uma grande quantidade de objetos;
- os custos de armazenamento são altos por causa da grande
quantidade de objetos;
- a maioria dos estados de objetos podem se tornar extrínsecos;
- muitos objetos podem ser substituídos por poucos objetos
compartilhados;
- a aplicação não depende de identidade dos objetos.

IMPORTANTE:
- Estado intríseco é o estado do objeto que não muda nada, 
esse estado deve estar dentro do objeto flyweight;
- Estado extrínseco é o estado do objeto que muda, esse estado
pode ser movido para fora do objeto flyweight;

DICIONÁRIO:
Intríseco - que faz parte de ou que constitui a essência,
a natureza de algo; que é próprio de algo; inerente.
Extrínseco - que não pertence à essência de algo, que é
exterior.
"""

from __future__ import annotations
from typing import List, Dict


class Client:
    """CONTEXT"""
    def __init__(self, name: str) -> None:
        self.name = name
        self._addresses: List = []

        #Extrinsic adress data
        self.address_number: str
        self.address_details: str
    
    def add_address(self, address: Address) -> None:
        self._addresses.append(address)
    
    def list_addresses(self) -> None:
        for address in self._addresses:
            address.show_address(self.address_number, self.address_details)


class Address:
    '''Flyweight'''
    def __init__(self, street: str, neighborhood: str, zip_code: str) -> None:
        self._street = street
        self._neighborhood = neighborhood
        self._zip_code = zip_code
    
    def show_address(self, address_number: str, address_details: str) ->None:
        print(
            self._street,
            address_number,
            self._neighborhood,
            address_details,
            self._zip_code
        )

class AddressFactory:
    _addresses: Dict = {}

    def _get_key(self, **kwargs) ->str:
        return ''.join(kwargs.values())
    
    def get_address(self, **kwargs) ->Address:
        key = self._get_key(**kwargs)

        try:
            address_flyweight = self._addresses[key]
            print('usando objeto já criado')
        except KeyError:
            address_flyweight = Address(**kwargs)
            self._addresses[key] = address_flyweight
            print('criando novo objeto')

            return address_flyweight
        

if __name__ == "__main__":
    address_factory = AddressFactory()

    a1 = address_factory.get_address(
        street='Av Brasil',
        neighborhood='Centro',
        zip_code='000000-000'
    )

    a2 = address_factory.get_address(
        street='Av Brasil ',
        neighborhood='Centro',
        zip_code='000000-000'
    )
    
    gdias = Client('Gabriel')
    gdias.address_number = '11'
    gdias.address_details = 'Casa'
    gdias.add_address(a1)
    gdias.list_addresses()

    joana = Client('joana')
    joana.address_number = '250A'
    joana.address_details = 'AP 555'
    joana.add_address(a2)
    joana.list_addresses()

    print(a1 == a2)
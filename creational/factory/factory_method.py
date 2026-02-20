from abc import ABC, abstractmethod


class Veiculo(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None: pass


class CarroLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print('Carro de luxo está buscando o cliente...')


class CarroPopular(Veiculo):
    def buscar_cliente(self) -> None:
        print('Carro popular está buscando o cliente...')


class Moto(Veiculo):
    def buscar_cliente(self) -> None:
        print('moto indo buscar o cliente...')


class VeiculoFactory(ABC):
    def __init__(self, tipo):
        self.carro = self.get_carro(tipo)

    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        if tipo == 'luxo':
            return CarroLuxo()
        if tipo == 'popular':
            return CarroPopular()
        if tipo == 'moto':
            return Moto()
        assert 0, 'veiculo não existe'

    def buscar_cliente(self):
        self.carro.buscar_cliente()

class LuisCorreiaVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro(tipo: str) -> None:
        if tipo == 'luxo':
            return CarroLuxo()
        if tipo == 'popular':
            return CarroPopular()
        if tipo == 'moto':
            return Moto()
        assert 0, 'veiculo não existe'    

class PhbVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro(tipo: str) -> None:
        if tipo == 'luxo':
            return CarroLuxo()
        if tipo == 'popular':
            return CarroPopular()
        assert 0, 'veiculo não existe'  


if __name__ == "__main__":
    from random import choice
    veiculoo_disponiveis_LC = ['luxo', 'popular','moto']
    veiculoo_disponiveis_PHB = ['luxo', 'popular']

    print('Luis Correia')
    for i in range(10):
        carro = LuisCorreiaVeiculoFactory(
            choice(veiculoo_disponiveis_LC))
        carro.buscar_cliente()

    print('----------')

    print('Parnaíba')
    for i in range(10):
        carro = PhbVeiculoFactory(
            choice(veiculoo_disponiveis_PHB))
        carro.buscar_cliente()
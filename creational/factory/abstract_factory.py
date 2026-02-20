from abc import ABC, abstractmethod


class VeiculoLuxo(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None: pass

class VeiculoPopular(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None: pass


class CarroLuxoLC(VeiculoLuxo):
    def buscar_cliente(self) -> None:
        print('Carro de luxo LC está buscando o cliente...')


class CarroPopularLC(VeiculoPopular):
    def buscar_cliente(self) -> None:
        print('Carro popular LC está buscando o cliente...')


class MotoLC(VeiculoPopular):
    def buscar_cliente(self) -> None:
        print('moto popular LC indo buscar o cliente...')

class CarroLuxoPHB(VeiculoLuxo):
    def buscar_cliente(self) -> None:
        print('Carro de luxo PHB está buscando o cliente...')


class CarroPopularPHB(VeiculoPopular):
    def buscar_cliente(self) -> None:
        print('Carro popular PHB está buscando o cliente...')


class MotoPHB(VeiculoPopular):
    def buscar_cliente(self) -> None:
        print('moto popular PHB indo buscar o cliente...')

class VeiculoFactory(ABC):
    @staticmethod
    @abstractmethod
    def get_carro_luxo() -> VeiculoLuxo: pass
    @staticmethod
    @abstractmethod
    def get_carro_popular() -> VeiculoPopular: pass
    @staticmethod
    @abstractmethod
    def get_moto_popular() -> VeiculoPopular: pass

class LuisCorreiaVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro_luxo() -> VeiculoLuxo:
        return CarroLuxoLC()

    @staticmethod
    def get_carro_popular() -> VeiculoPopular:
        return CarroPopularLC()

    @staticmethod
    def get_moto_popular() -> VeiculoPopular:
        return MotoLC()

class PhbVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro_luxo() -> VeiculoLuxo:
        return CarroLuxoPHB()

    @staticmethod
    def get_carro_popular() -> VeiculoPopular:
        return CarroPopularPHB()

    @staticmethod
    def get_moto_popular() -> VeiculoPopular:
        return MotoPHB()

class Cliente:
    def busca_clientes(self):
        for factory in [LuisCorreiaVeiculoFactory(), PhbVeiculoFactory()]:
            carro_popular = factory.get_carro_popular()
            carro_popular.buscar_cliente()

            carro_luxo = factory.get_carro_luxo()
            carro_luxo.buscar_cliente()

            moto_popular = factory.get_moto_popular()
            moto_popular.buscar_cliente()


if __name__ == "__main__":
    cliente = Cliente()
    cliente.busca_clientes()
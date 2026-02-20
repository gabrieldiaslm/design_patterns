'''
template method - principio da inversão de controle
OPK's secret weapon
'''


from abc import ABC, abstractmethod


class Pizza(ABC):
    '''classe abstrata'''
    def prepare(self) -> None:
        '''template method'''
        self.hook_before_add_ingrendients() #hook 
        self.add_ingredients() # abstract
        self.hook_after_add_ingrendients() #hook
        self.cook() # abstract
        self.cut() # metodo concreto
        self.serve() # metodo concreto

    def hook_before_add_ingrendients(self): pass
    def hook_after_add_ingrendients(self): pass


    def cut(self):
        print(f'{self.__class__.__name__}: Cortando pizza')
    def serve(self):
        print(f'{self.__class__.__name__}: Servindo pizza')
    
    @abstractmethod
    def add_ingredients(self): pass

    @abstractmethod
    def cook(self): pass

class ModaDaCasa(Pizza):
    def add_ingredients(self):
        print('ModaDaCasa: adicionando ingredientes (presunto, queijo, goiabada)')
    
    def cook(self):
        print('ModaDaCasa: cozinhando por 45 minutos no forno a lenha')


class Vegana(Pizza):
    def hook_before_add_ingrendients(self):
        print(f'{self.__class__.__name__}: Lavando ingredientes')
    def add_ingredients(self):
        print(f'{self.__class__.__name__}: adicionando ingredientes (rúcula, manjericão, tomate)')
    
    def cook(self):
        print(f'{self.__class__.__name__}: cozinhando por 30 minutos no forno normal')


if __name__ == "__main__":
    a_moda = ModaDaCasa()
    a_moda.prepare()
    print('--'*20)
    veg = Vegana()
    veg.prepare()
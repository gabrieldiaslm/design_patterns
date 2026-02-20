'''
template method - principio da inversão de controle
OPK's secret weapon
'''


from abc import ABC, abstractmethod


class Abstract(ABC):
    def template_method(self):
        self.hook()
        self.operation1()
        self.base_class_method()
        self.operation2()
    
    def hook(self): pass

    def base_class_method(self):
        print('EU SEREI EXECUTADO (abstract class)')

    @abstractmethod
    def operation1(self): pass

    @abstractmethod
    def operation2(self): pass


class ConcreteClass1(Abstract):
    def hook(self):
        print('TEMA O PODER, QUE VOCÊ NÃO VÊ')

    def operation1(self): 
        print('OP 1 CONCLUIDA')

    def operation2(self): 
        print('OP 2 CONCLUIDA')

class ConcreteClass2(Abstract):
    def operation1(self): 
        print('OP 1 CONCLUIDA (True ending)')

    def operation2(self): 
        print('OP 2 CONCLUIDA (True ending)')

if __name__ == "__main__":
    c1 = ConcreteClass1()
    c1.template_method()
    print('...')
    c2 = ConcreteClass2()
    c2.template_method()
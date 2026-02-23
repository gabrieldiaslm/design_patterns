'''
o padrão de projeto state é um padrão comportamental
que tem a intenção de permitir a um objeto mudar seu 
comportamento quando o seu estado interno muda.
o objeto parecerá ter mudado sua classe.
'''
from __future__ import annotations
from abc import ABC, abstractmethod
class Order:
    '''context'''
    def __init__(self) -> None:
        self.state = OrderState = PaymentPending(self)
    
    def pending(self) -> None:
        ('tentando executar pending()')
        self.state.pending()

    def approve(self) -> None:
        ('tentando executar aprove()')
        self.state.approve()

    def reject(self) -> None:
        ('tentando executar reject()')
        self.state.reject()


class OrderState(ABC):
    def __init__(self, order: Order) -> None:
        self.order = order
    
    @abstractmethod
    def pending(self) -> None: pass
    
    @abstractmethod
    def approve(self) -> None: pass
    
    @abstractmethod
    def reject(self) -> None: pass

    def __str__(self):
        return __class__.__name__

class PaymentPending(OrderState):
    
    def pending(self) -> None: 
        print('pagamento já pendente.')
    
    def approve(self) -> None:
        self.order.state = PaymentApproved(self.order)
        print('pagamento aprovado!')
    
    def reject(self) -> None: 
        self.order.state = PaymentRejected(self.order)
        print('pagamento recusado!')

class PaymentApproved(OrderState):
    
    def pending(self) -> None:
        self.order.state = PaymentPending(self.order)
        print('pagamento pendente!')
    
    def approve(self) -> None:
        print('pagamento já aprovado.')
    
    def reject(self) -> None:
        self.order.state = PaymentRejected(self.order)
        print('pagamento recusado!')

class PaymentRejected(OrderState):
    
    def pending(self) -> None:
        print('pagamento já está recusado, não há o que ser feito...')

    def approve(self) -> None:
        print('pagamento já está recusado, não há o que ser feito...')
    
    def reject(self) -> None: 
        print('pagamento já está recusado.')

if __name__ == "__main__":
    print("*"*5,'S T A T E',"*"*5)
    order = Order()
    order.pending()
    order.approve()
    order.pending()
    order.reject()
    order.pending()
    order.approve()
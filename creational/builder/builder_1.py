from abc import ABC, abstractmethod


class User:
    def __init__(self):
        self.firstname = None
        self.lastname = None
        self.age = None
        self.phone_numbers = []
        self.address = []

class IUserBuilder(ABC):
    @property
    @abstractmethod
    def result(self): pass

    @abstractmethod
    def add_firstname(self, firstname): pass

    @abstractmethod
    def add_lastname(self, lastname): pass

    @abstractmethod
    def add_age(self, age): pass
    
    @abstractmethod
    def add_phone(self, phone): pass

    @abstractmethod
    def add_address(self, address): pass

class UserBuilder(IUserBuilder):
    def __init__(self):
        self.reset()

    def reset(self):
        self._result = User()

    @property
    def result(self):
        return_data = self._result
        self.reset()
        return return_data 

    def add_firstname(self, firstname):
        self._result.firstname = firstname

    def add_lastname(self, lastname): 
        self._result.lastname = lastname

    def add_age(self, age): 
        self.result.age = age
    
    def add_phone(self, phone): 
        self._result.phone_numbers.append(phone)

    def add_address(self, address): 
        self._result.address.append(address)

class UserDirector:
    def __init__(self, builder: UserBuilder):
        self._builder = builder

    def with_age(self, firstname, lastname, age):
        self._builder.add_firstname(firstname)
        self._builder.add_lastname(lastname)
        self._builder.add_age(age)
        return self._builder.result
    
if __name__ == "__main__":
    user_builder = UserBuilder()
    user_director = UserDirector(user_builder)
    user1 = user_director.with_age('Ga', 'Dias', 22)
    print(user1.firstname, user1.lastname)
    print(user1)
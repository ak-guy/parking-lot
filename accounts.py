# from abc import abstractmethod, ABC
from . import Person
class Account:
    def __init__(self, user_name, password, person: Person, account_status):
        self.__user_name: str = user_name
        self.__password: str = password
        self.__person: Person = person
        self.__account_status: int = account_status

class Admin(Account):
    def __init__(self, user_name: str, password: str, person: Person, account_status):
        super().__init__(user_name, password, person, account_status)
    
    
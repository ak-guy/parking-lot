# from abc import abstractmethod, ABC
from utils import Person

class Account:
    def __init__(self, user_name, password, person: Person, account_status):
        self.__user_name: str = user_name
        self.__password: str = password
        self.__person: Person = person
        self.__account_status: int = account_status

class Admin(Account):
    def __init__(self, user_name: str, password: str, person: Person, account_status):
        super().__init__(user_name, password, person, account_status)
    
    def add_parking_floor(self):
        pass

    def add_parking_spot(self):
        pass

    def add_display_board(self):
        pass

    def add_entrance_panel(self):
        '''can make payment here too, also free parking spot will be shown in this'''
        pass

    def add_exit_panel(self):
        '''can make payment here'''
        pass

class Attendent(Account):
    def __init__(self, user_name: str, password: str, person: Person, account_status):
        super().__init__(user_name, password, person, account_status)

    def process_cash(self):
        pass
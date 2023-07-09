from enum import Enum

class PaymentStatus(Enum):
    COMPLETED = 1 
    FAILED = 2
    PENDING = 3
    UNPAID = 4
    REFUNDED = 5

class AccountStatus(Enum):
    ACTIVE = 1
    CLOSED = 2
    CANCELED = 3 
    BLACKLISTED = 4
    NONE = 5

class Person():
    def __init__(self, name, address, phone, email):
        self.__name = name
        self.__address = address
        self.__email = email
        self.__phone = phone

class Adress():
    def __init__(self, zip_code, address, city, state, country):
        self.__zip_code = zip_code
        self.__address = address
        self.__city = city
        self.__state = state
        self.__country = country
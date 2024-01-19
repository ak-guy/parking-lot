from abc import ABC, abstractmethod

class Address(ABC):
    @abstractmethod
    def __init__(self):
        pass

class IAddressA(Address):
    def __init__(self, house_number: str, street: str, city: str, state: str, zip_code: int, country: str):
        self.__house_number = house_number
        self.__street = street
        self.__city = city
        self.__state = state
        self.__zip_code = zip_code
        self.__country = country

class IAddressB(Address):
    def __init__(self, house_number: str, block: str, sector: int, city: str, state: str, zip_code: int, country: str):
        self.__house_number = house_number
        self.__block = block
        self.__sector = sector
        self.__city = city
        self.__state = state
        self.__zip_code = zip_code
        self.__country = country

class Person:
    def __init__(self, name: str, address: Address, phone_number: str, email: str):
        self.__name = name
        self.__address = address
        self.__phone_number = phone_number
        self.__email = email


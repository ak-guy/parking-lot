from abc import ABCMeta, abstractmethod


class Vehicle(ABCMeta):
    def __init__(self, license_no):
        self.license_no = license_no
    
    # we will asign ticket to vehicle
    @abstractmethod
    def assign_ticket(self, ticket): # ticket -> instance of ParkingTicket class
        pass

class Car(Vehicle):
    def __init__(self, license_no):
        super().__init__(self.license_no)

    def assign_ticket(self, ticket): # ticket -> instance of ParkingTicket class
        pass

class Bike(Vehicle):
    def __init__(self, license_no):
        super().__init__(self.license_no)

    def assign_ticket(self, ticket): # ticket -> instance of ParkingTicket class
        pass

class Truck(Vehicle):
    def __init__(self, license_no):
        super().__init__(self.license_no)

    def assign_ticket(self, ticket): # ticket -> instance of ParkingTicket class
        pass

class Van(Vehicle):
    def __init__(self, license_no):
        super().__init__(self.license_no)

    def assign_ticket(self, ticket): # ticket -> instance of ParkingTicket class
        pass

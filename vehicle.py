from constants import VehicleType

class Vehicle:
    def __init__(self, registration_number: str, vehicle_type: VehicleType):
        self.__registration_number = registration_number
        self.__vehicle_type = vehicle_type

    def assign_ticket(self):
        pass

class Car(Vehicle):
    def __init__(self, registration_number: str):
        super().__init__(VehicleType.CAR)

class Bike(Vehicle):
    def __init__(self, registration_number: str):
        super().__init__(VehicleType.BIKE)

class Truck(Vehicle):
    def __init__(self, registration_number: str):
        super().__init__(VehicleType.TRUCK)

class ElectricCar(Vehicle):
    def __init__(self, registration_number: str):
        super().__init__(VehicleType.ELECTRIC_CAR)

class Van(Vehicle):
    def __init__(self, registration_number: str):
        super().__init__(VehicleType.VAN)
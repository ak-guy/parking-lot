from abc import ABC, abstractmethod
from constants import ParkingSpotType
from vehicle import Vehicle

'''
Here using an Interface for creating different parking spots does not make any sense
because then we need to implement is_free, assign_spot and remove_spot for every type of
parking spots

class IParkingSpot(ABC):
    def __init__(self, number, parking_spot_type):
        self.__number = number
        self.__parking_spot_type = parking_spot_type
        self.__free = True
        self.__vehicle = None

    @abstractmethod
    def is_free(self):
        pass

    @abstractmethod
    def assign_spot(self):
        pass

    @abstractmethod
    def remove_spot(self):
        pass

class IParkingSpotCompact(IParkingSpot):
    def __init__(self, number):
        super().__init__(number, ParkingSpotType.COMPACT)
    
    def is_free(self):
        return self.__free
    
    def assign_spot(self, vehicle: IVehicle):
        self.__free = False
        self.__vehicle = vehicle

    def remove_spot(self):
        self.__free = True
        self.__vehicle = None

class IParkingSpotLarge(IParkingSpot):
    def __init__(self, number):
        super().__init__(number, ParkingSpotType.LARGE)
    
    def is_free(self):
        return self.__free
    
    def assign_spot(self, vehicle: IVehicle):
        self.__free = False
        self.__vehicle = vehicle

    def remove_spot(self):
        self.__free = True
        self.__vehicle = None

class IParkingSpotHandicapped(IParkingSpot):
    def __init__(self, number):
        super().__init__(number, ParkingSpotType.HANDICAPPED)
    
    def is_free(self):
        return self.__free
    
    def assign_spot(self, vehicle: IVehicle):
        self.__free = False
        self.__vehicle = vehicle

    def remove_spot(self):
        self.__free = True
        self.__vehicle = None

class IParkingSpotElectric(IParkingSpot):
    def __init__(self, number):
        super().__init__(number, ParkingSpotType.ELECTRIC)
    
    def is_free(self):
        return self.__free
    
    def assign_spot(self, vehicle: IVehicle):
        self.__free = False
        self.__vehicle = vehicle

    def remove_spot(self):
        self.__free = True
        self.__vehicle = None

class IParkingSpotBike(IParkingSpot):
    def __init__(self, number):
        super().__init__(number, ParkingSpotType.BIKE)
    
    def is_free(self):
        return self.__free
    
    def assign_spot(self, vehicle: IVehicle):
        self.__free = False
        self.__vehicle = vehicle

    def remove_spot(self):
        self.__free = True
        self.__vehicle = None
'''

class ParkingSpot:
    def __init__(self, number, parking_spot_type):
        self.__number = number
        self.__parking_spot_type = parking_spot_type
        self.__free = True
        self.__vehicle = None

    def is_free(self):
        return self.__free
    
    def assign_spot(self, vehicle: Vehicle):
        self.__free = False
        self.__vehicle = vehicle

    def remove_spot(self):
        self.__free = True
        self.__vehicle = None

class ParkingSpotCompact(ParkingSpot):
    def __init__(self, number):
        super().__init__(number, ParkingSpotType.COMPACT)

class ParkingSpotLarge(ParkingSpot):
    def __init__(self, number):
        super().__init__(number, ParkingSpotType.LARGE)

class ParkingSpotHandicapped(ParkingSpot):
    def __init__(self, number):
        super().__init__(number, ParkingSpotType.HANDICAPPED)

class ParkingSpotElectric(ParkingSpot):
    def __init__(self, number):
        super().__init__(number, ParkingSpotType.ELECTRIC)

class ParkingSpotBike(ParkingSpot):
    def __init__(self, number):
        super().__init__(number, ParkingSpotType.BIKE)

if __name__ == '__main__':
    parking_obj = ParkingSpotCompact(12)
    print(parking_obj.__dict__)
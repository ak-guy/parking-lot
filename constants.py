from enum import Enum

class VehicleType(Enum):
    CAR = 1
    BIKE = 2
    TRUCK = 3
    ELECTRIC_CAR = 4
    VAN = 5

class ParkingSpotType(Enum):
    COMPACT = 1
    LARGE = 2
    HANDICAPPED = 3
    ELECTRIC = 4
    BIKE = 5

class ParkingTicketStatus(Enum):
    ACTIVE = 1
    EXPIRED = 2

class AccountStatus(Enum):
    ACTIVE = 1
    BLOCKED = 2
    UNKNOWN = 3
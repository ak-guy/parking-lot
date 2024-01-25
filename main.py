from parking_floor import ParkingFloor
from info_panel import InfoPanel

class SingletonParkingLot(type):
    _instance = {}

    def __call__(self, *args, **kwargs):
        if self not in self._instance:
            new_instance = super().__call__(*args, **kwargs)
            self._instance[self] = new_instance

        return self._instance[self]

class ParkingLot(metaclass=SingletonParkingLot):
    def __init__(self, name: str, address: str):
        self._name = name
        self._address = address
        self._parking_floor = [ParkingFloor()]
        self._info_panel = InfoPanel()

    def addParkingFloor(self):
        '''will be responsible for creating ParkingFloor objects'''
        new_parking_floor = ParkingFloor('Ground')
        self._parking_floor.append(new_parking_floor)
    
    '''
    decided to keep only one InfoPanel for a single ParkingLot
    but can create multiple Entrance and Exit Panel for each floor
    def addInfoPanel(self):
        new_info_panel = InfoPanel()
        self._info_panel.append(new_info_panel)
    '''
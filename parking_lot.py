from parking_floor import ParkingFloor

class SingletonParkingLot(type):
    _instance = {}

    def __call__(self, *args, **kwargs):
        if self not in self._instance:
            new_instance = super().__call__(*args, **kwargs)
            self._instance[self] = new_instance

        return self._instance[self]
    
class _InfoPanel:
    '''_InfoPanel will be observing all Entrance Panel'''
    def __init__(self, parking_lot_obj):
        self._total_free_compact_spots = 0
        self._total_free_large_spots = 0
        self._total_free_handicapped_spots = 0
        self._total_free_electric_spots = 0
        self._total_free_bike_spots = 0
        self.get_updated_empty_parking_slots(parking_lot_obj)

    def get_updated_empty_parking_slots(self, parking_lot_obj):
        parking_floor_list = SingletonParkingLot._instance[parking_lot_obj]._parking_floor
        for parking_floor in parking_floor_list:
            self._total_free_compact_spots += parking_floor.__free_compact_spots
            self._total_free_large_spots += parking_floor.__free_large_spots
            self._total_free_handicapped_spots += parking_floor.__free_handicapped_spots
            self._total_free_electric_spots += parking_floor.__free_electric_spots
            self._total_free_bike_spots += parking_floor.__free_bike_spots
    
    def get_notified(self, compact=None, large=None, handicapped=None, electric=None, bike=None):
        if compact:
            self._total_free_compact_spots += compact
        if large:
            self._total_free_large_spots += large
        if handicapped:
            self._total_free_handicapped_spots += handicapped
        if electric:
            self._total_free_electric_spots += electric
        if bike:
            self._total_free_bike_spots += bike
        
        self.show_message()

    def show_messsage(self):
        panel_msg = ''
        if self._total_free_compact_spots:
            panel_msg += f'Total Number of free compact spots = {self._total_free_compact_spots}'
        else:
            panel_msg += f'No compact spots available'
        
        panel_msg += '\n'

        if self._total_free_large_spots:
            panel_msg += f'Total Number of free large spots = {self._total_free_large_spots}'
        else:
            panel_msg += f'No large spots available'
        
        panel_msg += '\n'

        if self._total_free_handicapped_spots:
            panel_msg += f'Total Number of free handicapped spots = {self._total_free_handicapped_spots}'
        else:
            panel_msg += f'No handicapped spots available'
        
        panel_msg += '\n'

        if self._total_free_electric_spots:
            panel_msg += f'Total Number of free electric spots = {self._total_free_electric_spots}'
        else:
            panel_msg += f'No electric spots available'
        
        panel_msg += '\n'

        if self._total_free_bike_spots:
            panel_msg += f'Total Number of free bike spots = {self._total_free_bike_spots}'
        else:
            panel_msg += f'No bike spots available'
        
        # send data to frontend
        return panel_msg
        

class ParkingLot(metaclass=SingletonParkingLot):
    def __init__(self, name: str, address: str):
        self._name = name
        self._address = address
        self._parking_floor = []
        self._info_panel = _InfoPanel(self)

    def createParkingFloor(self, floor_name,
                           number_of_compact_spots,
                           number_of_large_spots,
                           number_of_handicapped_spots,
                           number_of_electric_spots,
                           number_of_bike_spots):
        parking_floor_obj = ParkingFloor(floor_name=floor_name)
        parking_floor_obj.addParkingSpot(number_of_compact_spots,
                                         number_of_large_spots,
                                         number_of_handicapped_spots,
                                         number_of_electric_spots,
                                         number_of_bike_spots)
        self.addParkingFloor(parking_floor_obj)


    def addParkingFloor(self, new_parking_floor: ParkingFloor):
        '''will be responsible for adding ParkingFloor objects'''
        self._parking_floor.append(new_parking_floor)
    
    '''
    decided to keep only one InfoPanel for a single ParkingLot
    but can create multiple Entrance and Exit Panel for each floor
    def addInfoPanel(self):
        new_info_panel = InfoPanel()
        self._info_panel.append(new_info_panel)
    '''
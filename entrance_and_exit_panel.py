from vehicle import Vehicle

class EntrancePanel:
    '''
       responsible for creating ticket, alloting and displaying parking spot, 
       also there can be multiple Entrance Panel at each floor
    '''
    def __init__(self, parking_floor_obj):
        self._parking_floor_obj = parking_floor_obj

    def generate_ticket(self, vehicle: Vehicle):
        pass

    def assign_spot(self):
        pass

    def reduce_parking_spot_count(self):
        pass

class ExitPanel:
    '''
        responsible for processing ticket and generating receipt
    '''
    def process_ticket(self):
        pass

    def generate_receipt(self):
        pass

    def open_barrier(self):
        pass
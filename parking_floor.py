class ParkingFloor:
    def __init__(self):
        self.__compact_spots = {}
        self.__large_spots = {}
        self.__handicapped_spots = {}
        self.__electric_spots = {}
        self.__bike = {}

        self.__info_portals = {}

        self.__free_compact_spots = {'free':0}
        self.__free_large_spots = {'free':0}
        self.__free_handicapped_spots = {'free':0}
        self.__free_electric_spots = {'free':0}
        self.__free_bike_spots = {'free':0}

    
from abc import ABC, abstractmethod
from parking_spot import AddCompactSpot, AddLargeSpot, AddHandicappedSpot, AddElectricSpot, AddBikeSpot

class ParkingFloor:
    def __init__(self, floor_name: str):
        self.__name = floor_name
        self.__compact_spots = {}
        self.__large_spots = {}
        self.__handicapped_spots = {}
        self.__electric_spots = {}
        self.__bike = {}

        self.__entrance_panel = {}
        self.__exit_panel = {}

        self.__free_compact_spots = 0
        self.__free_large_spots = 0
        self.__free_handicapped_spots = 0
        self.__free_electric_spots = 0
        self.__free_bike_spots = 0

    def addParkingSpot(self, compact: int, large:int, handicapped: int, electric: int, bike: int):
        if compact:
            AddCompactSpot.addSpot(compact, self)
            self.__free_compact_spots += compact
        if large:
            AddLargeSpot.addSpot(large, self)
            self.__free_large_spots += large
        if handicapped:
            AddHandicappedSpot.addSpot(handicapped, self)
            self.__free_handicapped_spots += handicapped
        if electric:
            AddElectricSpot.addSpot(electric, self)
            self.__free_electric_spots += electric
        if bike:
            AddBikeSpot.addSpot(bike, self)
            self.__free_bike_spots += bike
    
    def addEntrancePanel(self):
        pass

    def addExitPanel(self):
        pass
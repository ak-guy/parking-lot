from abc import ABC, abstractmethod
from parking_spot import *

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

        self.__free_compact_spots = {'free':0}
        self.__free_large_spots = {'free':0}
        self.__free_handicapped_spots = {'free':0}
        self.__free_electric_spots = {'free':0}
        self.__free_bike_spots = {'free':0}

    def addParkingSpot(self, compact: int, large:int, handicapped: int, electric: int, bike: int):
        if compact:
            AddCompactSpot.addSpot(compact, self)
        if large:
            AddLargeSpot.addSpot(large, self)
        if handicapped:
            AddHandicappedSpot.addSpot(handicapped, self)
        if electric:
            AddElectricSpot.addSpot(electric, self)
        if bike:
            AddBikeSpot.addSpot(bike, self)
    
    def addEntrancePanel(self):
        pass

    def addExitPanel(self):
        pass
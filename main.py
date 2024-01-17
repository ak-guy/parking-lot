class SingletonParkingLot(type):
    _instance = {}

    def __call__(self, *args, **kwargs):
        if self not in self._instance:
            new_instance = super().__call__(*args, **kwargs)
            self._instance[self] = new_instance

        return self._instance[self]

class ParkingLot(metaclass=SingletonParkingLot):
    def __init__(self, name: str, address: str):
        self.name = name
        self.address = address

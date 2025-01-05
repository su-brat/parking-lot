# builder pattern

from level import Level
from parking_lot import ParkingLot
from parking_spot import ParkingSpot


class ParkingLotBuilder:
    def __init__(self):
        self.levels = {}

    def add_level(self, floor_id):
        if floor_id in self.levels:
            raise Exception("Level already exists with the given floor id")
        self.levels[floor_id] = Level(floor_id)
        return self

    def add_spots(self, floor_id, spots):
        if floor_id in self.levels:
            self.levels[floor_id].add_spots(spots)
            return self
        raise Exception("No such level found with given floor id")

    def add_spot(self, floor_id, vehicle_type):
        spot = ParkingSpot(vehicle_type)
        if floor_id in self.levels:
            self.levels[floor_id].add_spot(spot)
            return self
        else:
            raise Exception("No level found with the given floor id")

    def build(self):
        return ParkingLot(self.levels)

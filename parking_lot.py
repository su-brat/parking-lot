# parking lot main module
from level import Level
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


class ParkingLot:
    def __init__(self, levels):
        self.levels = levels

    def get_available_spots(self, vehicle=None):
        spots = []
        for level in self.levels.values():
            spots.extend(level.get_available_spots(vehicle))
        return spots

    def park_vehicle(self, vehicle):
        spots = self.get_available_spots(vehicle)
        if len(spots) > 0:
            first_spot = spots[0]
            first_spot.park_vehicle(vehicle)
            return first_spot
        else:
            raise Exception("No available spot")

    def unpark_vehicle(self, vehicle):
        for level in self.levels.values():
            parked_spot = level.get_parked_spot(vehicle)
            if parked_spot is not None:
                parked_spot.unpark_vehicle()
                return parked_spot
        raise Exception("Vehicle not found")

    def display_availability(self, vehicle):
        return len(self.get_available_spots(vehicle)) > 0

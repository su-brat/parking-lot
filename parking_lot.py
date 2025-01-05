# parking lot main module


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

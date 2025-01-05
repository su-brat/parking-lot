class Level:
    def __init__(self, floor_id, spots=None):
        self.floor_id = floor_id
        self.spots = spots if spots is not None else []

    def add_spot(self, spot):
        self.spots.append(spot)

    def add_spots(self, spots):
        self.spots.extend(spots)

    def get_available_spots(self, vehicle=None):
        spots = []
        for spot in self.spots:
            if vehicle is None:
                if spot.is_available():
                    spots.append(spot)
            elif vehicle.get_type() == spot.get_vehicle_type():
                if spot.is_available():
                    spots.append(spot)
        return spots

    def get_parked_spot(self, vehicle):
        for spot in self.spots:
            if spot.is_vehicle_parked(vehicle):
                return spot
        return None

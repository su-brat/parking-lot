class ParkingSpot:
    instance_cnt = 0

    def __init__(self, vehicle_type, vehicle=None):
        ParkingSpot.instance_cnt += 1
        self.spot_id = ParkingSpot.instance_cnt
        self.vehicle_type = vehicle_type
        self.parked_vehicle = vehicle

    def is_parkable(self, vehicle):
        return vehicle.get_type() == self.vehicle_type

    def is_vehicle_parked(self, vehicle):
        return vehicle == self.parked_vehicle

    def park_vehicle(self, vehicle):
        if self.is_parkable(vehicle):
            self.parked_vehicle = vehicle
        else:
            raise Exception("Parking spot cannot accomodate vehicle type")

    def is_available(self):
        return self.parked_vehicle is None

    def get_spot_id(self):
        return self.spot_id

    def get_vehicle_type(self):
        return self.vehicle_type

    def get_parked_vehicle(self):
        return self.parked_vehicle

    def unpark_vehicle(self):
        if self.parked_vehicle:
            vehicle = self.parked_vehicle
            self.parked_vehicle = None
            return vehicle
        raise Exception("No vehicle parked at this spot")

    def clone(self):
        vehicle_type = self.vehicle_type
        parked_vehicle = self.parked_vehicle
        return ParkingSpot(vehicle_type, parked_vehicle)

    def __str__(self):
        return f"ParkingSpot(spot_id = {self.get_spot_id()}, vehicle_type = {self.get_vehicle_type()}, parked_vehicle = {self.get_parked_vehicle()}"

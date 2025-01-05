from vehicle import Vehicle
from vehicle_type import VehicleType


class Motorcycle(Vehicle):
    def __init__(self, license_no):
        super().__init__(license_no, VehicleType.MOTORCYCLE)

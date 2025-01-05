from motorcycle import Motorcycle
from car import Car
from truck import Truck
from vehicle_type import VehicleType


class VehicleFactory:
    vehicle_instance = {
        VehicleType.TRUCK: Truck,
        VehicleType.CAR: Car,
        VehicleType.MOTORCYCLE: Motorcycle,
    }

    def get_vehicle(self, vehicle_type, license_no):
        if vehicle_type in self.vehicle_instance:
            VehicleCls = self.vehicle_instance[vehicle_type]
            return VehicleCls(license_no)
        raise Exception("No such vehicle type found")

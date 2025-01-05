from abc import ABC

class Vehicle(ABC):
    def __init__(self, license_no, vehicle_type):
        self.license_no = license_no
        self.type = vehicle_type

    def get_type(self):
        return self.type

    def get_license(self):
        return self.license_no
# client main code

from parking_lot_builder import ParkingLotBuilder
from parking_spot import ParkingSpot
from vehicle_factory import VehicleFactory
from vehicle_type import VehicleType

if __name__ == "__main__":
    truck_spot = ParkingSpot(VehicleType.TRUCK)
    car_spot = ParkingSpot(VehicleType.CAR)
    motorcycle_spot = ParkingSpot(VehicleType.MOTORCYCLE)

    level1_spots = [truck_spot.clone(), truck_spot.clone(), car_spot.clone()]
    level2_spots = [truck_spot.clone(), car_spot.clone()]
    level3_spots = [
        truck_spot.clone(),
        car_spot.clone(),
        car_spot.clone(),
        motorcycle_spot.clone(),
        motorcycle_spot.clone(),
    ]

    parking_lot = (
        ParkingLotBuilder()
        .add_level(1)
        .add_level(2)
        .add_level(3)
        .add_spots(1, level1_spots)
        .add_spots(2, level2_spots)
        .add_spots(3, level3_spots)
        .build()
    )

    car1 = VehicleFactory().create_vehicle(VehicleType.CAR, "BH23A3JJ")
    car2 = VehicleFactory().create_vehicle(VehicleType.CAR, "BH22A2JJ")
    truck1 = VehicleFactory().create_vehicle(VehicleType.TRUCK, "BH23A3JI")
    motorcycle1 = VehicleFactory().create_vehicle(VehicleType.MOTORCYCLE, "BH23A3JA")
    motorcycle2 = VehicleFactory().create_vehicle(VehicleType.MOTORCYCLE, "BH23A3JB")
    motorcycle3 = VehicleFactory().create_vehicle(VehicleType.MOTORCYCLE, "BH23A3JC")

    print(parking_lot.park_vehicle(car1))
    print(parking_lot.park_vehicle(car2))
    print(parking_lot.park_vehicle(truck1))
    print(parking_lot.park_vehicle(motorcycle1))
    print(parking_lot.park_vehicle(motorcycle2))
    # print(parking_lot.park_vehicle(motorcycle3))

    print(parking_lot.unpark_vehicle(car1))
    print(parking_lot.unpark_vehicle(car2))
    print(parking_lot.unpark_vehicle(truck1))
    print(parking_lot.unpark_vehicle(motorcycle1))
    print(parking_lot.unpark_vehicle(motorcycle2))
    # print(parking_lot.unpark_vehicle(motorcycle3))

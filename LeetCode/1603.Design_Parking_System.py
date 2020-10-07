class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.cars = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        self.cars[carType - 1] -= 1
        if self.cars[carType - 1] >= 0:
            return True
        return False

from car_model import CarModel

class Car:
    def __init__(self, model: CarModel, color: str, serial: str) -> None:
        self.model = model
        self.color = color
        self.serial = serial

    def check_serial(self) -> None:
        return self.model.check_serial(self.serial)

from car_model import CarModel
from car import Car
import gc

if __name__ == "__main__":

    dx = CarModel("FIT DX")
    lx = CarModel("FIT LX", air=True, cruise_control=True, power_locks=True, tilt=True)

    car1 = Car(dx, "blue", "12345")
    car2 = Car(dx, "black", "12346")
    car3 = Car(lx, "red", "12347")

    print(id(lx))
    del lx
    del car3
    print(gc.collect())

    lx = CarModel("FIT LX", air=True, cruise_control=True, power_locks=True, tilt=True)
    print(id(lx))

    lx = CarModel("FIT LX")
    print(id(lx))
    print(lx.air)

    car3 = Car(lx, "red", "12347")
    car4 = Car(lx, "blue", "88847")
    print(id(car3))
    print(id(car4))
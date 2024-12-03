import weakref

# Flyweight Factory
class CarModel:
    # factory of car models (class attribute)
    _models = weakref.WeakValueDictionary()

    def __new__(cls, model_name: str, *args, **kwargs) -> "CarModel":
        model = cls._models.get(model_name)
        if not model:
            model = super().__new__(cls)
            cls._models[model_name] = model

        return model
    
    def __init__(self, model_name:str, air:bool=False, tilt:bool=False, 
                cruise_control:bool=False, power_locks:bool=False, 
                alloy_wheels:bool=False, usb_charger:bool=False) -> None:
        
        if not hasattr(self, "initted"):
            self.model_name = model_name
            self.air = air
            self.tilt = tilt
            self.cruise_control = cruise_control
            self.power_locks = power_locks
            self.alloy_wheels = alloy_wheels
            self.usb_charger = usb_charger
            self.initted=True

    def check_serial(self, serial_number:str) -> None:
        print("Sorry, we are unable to check "
            "the serial number {0} on the {1} "
            "at this time".format(serial_number, self.model_name))
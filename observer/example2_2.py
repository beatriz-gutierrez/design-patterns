from abc import ABC, abstractmethod

class Observer(ABC):

    def __call__(self):
        return NotImplementedError


class ConsoleObserver(Observer):

    def __call__(self, inventory: "Inventory"):
        print(f"Console output: product {inventory.product}",
              f"and quantitiy: {inventory.quantity}")


class BBDDObserver(Observer):
    
    def __call__(self, inventory: "Inventory"):
        print(f"BBBB output: product {inventory.product}",
              f"and quantitiy: {inventory.quantity}")


class Inventory:

    def __init__(self):
        self.observers = []
        self._product = None
        self._quantity = 0

    def register_observer(self, observer:"Observer"):

        if observer in self.observers:
            print(f"{observer} observer already in subscribed observers list.")

        self.observers.append(observer)

    def unregister_observer(self, observer:"Observer"):
        try:
            self.observers.remove(observer)
        except ValueError:
            print(f"{observer} observer not in subscribed observers list.")

    def notify_observers(self):
        for observer in self.observers:
            observer(self)

    @property
    def product(self):
        return self._product

    @product.setter
    def product(self, value):
        self._product = value
        self.notify_observers()

    @property 
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value
        self.notify_observers()


if __name__ == "__main__":

    inventoryA = Inventory()

    console_observer = ConsoleObserver()
    bbdd_observer = BBDDObserver()

    inventoryA.register_observer(console_observer)
    inventoryA.register_observer(bbdd_observer)

    inventoryA.product = "table1"
    inventoryA.quantity = 10

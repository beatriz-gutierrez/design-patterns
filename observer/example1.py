from abc import ABC, abstractmethod
from datetime import datetime
from time import sleep

class Observer(ABC):

    @abstractmethod
    def notify(self, timestamp: datetime) -> None:
        pass


class UsaTimeObserver(Observer):

    def __init__(self, name: str):
        self._name = name

    def notify(self, timestamp: datetime) -> None:
        time = datetime.strftime(timestamp, "%Y-%m-%d %I:%M:%S%p")
        print(f" > Observer {self._name} says: {time}")


class EuTimeObserver(Observer):

    def __init__(self, name: str):
        self._name = name

    def notify(self, timestamp: datetime) -> None:
        time = datetime.strftime(timestamp, "%Y-%m-%d %H:%M:%S")
        print(f" > Observer {self._name} says: {time}")


class Subject:

    def __init__(self):
        self._observers = []
        self._current_time = None

    def register_observer(self, observer):
        
        if observer in self._observers:
            print(f"{observer} observer already in subscribed observers list.")
        
        self._observers.append(observer)

    def unregister_observer(self, observer):

        try:
            self._observers.remove(observer)
        except ValueError:
            print(f"{observer} observer not in subscribed observers list.")

    def notify_observers(self):

        self._current_time = datetime.now()

        for observer in self._observers:
            observer.notify(self._current_time)


if __name__ == "__main__":

    subject = Subject()

    print("Adding usa time observer")
    usa_observer = UsaTimeObserver("UsaTimeObserver")
    subject.register_observer(usa_observer)
    subject.notify_observers()
    sleep(2)

    print("Adding eu time observer")
    eu_observer = EuTimeObserver("EuTimeObserver")
    subject.register_observer(eu_observer)
    subject.notify_observers()
    sleep(2)

    print("Removing usa time observer")
    subject.unregister_observer(usa_observer)
    subject.notify_observers()

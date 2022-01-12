from abc import ABC, abstractmethod


class Subject(ABC):
    @abstractmethod
    def subscribe(self, observer):
        pass

    @abstractmethod
    def unsubscribe(self, observer):
        pass

    @abstractmethod
    def notify(self):
        pass


class Observer(ABC):
    @abstractmethod
    def update(self, event):
        pass


class ISubject(Subject):
    def __init__(self):
        self._observers = []


    @property
    def observers(self):
        return self._observers


    def subscribe(self, observer):
        self.observers.append(observer)


    def unsubscribe(self, observer):
        self.observers.remove(observer)


    def notify(self, event):
        print("notificando evento:")
        print("\tCÓDIGO: " + str(event["codigo"]))
        print("\tDESCRIÇÃO: " + event["descricao"])
        print()
        for observer in self.observers:
            observer.update(event)

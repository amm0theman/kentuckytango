import abc


class IShipState:
    @abc.abstractmethod
    def move(self):
        pass

    @abc.abstractmethod
    def shoot(self):
        pass

    @abc.abstractmethod
    def intersect_event(self, arg):
        pass

    @abc.abstractmethod
    def render(self):
        pass


class IAsteroidState:
    @abc.abstractmethod
    def render(self):
        pass


class IBulletState:
    @abc.abstractmethod
    def render(self):
        pass

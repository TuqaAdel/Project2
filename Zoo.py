from abc import ABC, abstractmethod  # a module that provides the base for defining Abstract Base Classes "ABC"
import abc


# --------------- Strategy Pattern --------------- #
class Strategy:  # Strategy Interface
    __metaclass__ = abc.ABCMeta

    strategy = None

    def setStrategy(self, strategy):
        self.strategy = strategy

    def sleep(self):
        self.strategy.execute()


class Concrete(Strategy):
    def __init__(self, name):
        self.name = name

    def wakeUp(self):
        print(self.name + " the Cat Woke up")

    def makeNoise(self):
        print(self.name + " the Cat says meow")

    def eat(self):
        print(self.name + " the Cat is eating")

    def roam(self):
        print(self.name + " the Cat is running around")


class SleepBehavior:
    def execute(self):
        raise NotImplementedError

    __metaclass__ = abc.ABCMeta


class ConcreteMewo(SleepBehavior):
    def __init__(self, name):
        self.name = name

    def execute(self):
        print(self.name + " the Cat is mewoing")


class ConcreteRun(SleepBehavior):
    def __init__(self, name):
        self.name = name

    def execute(self):
        print(self.name + " the Cat is running around")


class ConcreteSleep(SleepBehavior):
    def __init__(self, name):
        self.name = name

    def execute(self):
        print(self.name + " the Cat is sleeping")

# --------------- End of Strategy Pattern --------------- #


# ------- Animals Abstract Class -------
class Animals(ABC):

    def __init__(self, name):
        self.name = name

    def wakeUp(self):
        print(self.name + " the " + self.__class__.__name__ + " Woke up")

    def makeNoise(self):
        pass

    def eat(self):
        print(self.name + " the " + self.__class__.__name__ + " is eating")

    def roam(self):
        pass

    def sleep(self):
        print(self.name + " the " + self.__class__.__name__ + " is sleeping")


# ------- Pachyderm Classes -------
class Pachyderm(Animals):
    def __init__(self, name):
        super().__init__(name)
        self.name = name

    def roam(self):
        print(self.name + " the " + self.__class__.__name__ + " is jumping")


class Rhino(Pachyderm):
    def __init__(self, name):
        super().__init__(name)
        self.name = name

    def makeNoise(self):
        print(self.name + " the " + self.__class__.__name__ + " is growling")


class Hippo(Pachyderm):
    def __init__(self, name):
        super().__init__(name)
        self.name = name

    def makeNoise(self):
        print(self.name + " the " + self.__class__.__name__ + " is grunting")


class Elephant(Pachyderm):
    def __init__(self, name):
        super().__init__(name)
        self.name = name

    def makeNoise(self):
        print(self.name + " the " + self.__class__.__name__ + " is trumpeting")


# ------- Feline Classes -------
class Feline(Animals):
    def __init__(self, name):
        super().__init__(name)
        self.name = name

    def roam(self):
        print(self.name + " the " + self.__class__.__name__ + " is running around")


class Tiger(Feline):
    def __init__(self, name):
        super().__init__(name)
        self.name = name

    def makeNoise(self):
        print(self.name + " the " + self.__class__.__name__ + " is chuffing")


class Lion(Feline):
    def __init__(self, name):
        super().__init__(name)
        self.name = name

    def makeNoise(self):
        print(self.name + " the " + self.__class__.__name__ + " is moaning")


class Cat(Feline):  # Delegates sleep behavior to Strategy
    def __init__(self, name):
        super().__init__(name)
        self.name = name


# No need to override sleep() method. Strategy will take care of it #


# ------- Canine Classes -------
class Canine(Animals):
    def __init__(self, name):
        super().__init__(name)
        self.name = name

    def roam(self):
        print(self.name + " the " + self.__class__.__name__ + " is seeking something")


class Wolf(Canine):
    def __init__(self, name):
        super().__init__(name)
        self.name = name

    def makeNoise(self):
        print(self.name + " the " + self.__class__.__name__ + " is bark-howling")


class Dog(Canine):
    def __init__(self, name):
        super().__init__(name)
        self.name = name

    def makeNoise(self):
        print(self.name + " the " + self.__class__.__name__ + " is barking")


# ----------- Observer Pattern ----------- #

class Subject:  # Subject/Observable interface

    def __init__(self):
        self._observers = []

    def register(self, observer):
        raise NotImplementedError

    def remove(self, observer):
        raise NotImplementedError

    def notify(self, message):
        raise NotImplementedError


class Observer(metaclass=abc.ABCMeta):  # Subscriber/Observer interface
    def update(self, message):
        pass


class ZooKeeper(Subject):
    def __init__(self, animals):
        super().__init__()
        self.allAnimals = animals

    def register(self, observer):
        self._observers.append(observer)

    def remove(self, observer):
        self._observers.remove(observer)

    def notify(self, message):
        for obs in self._observers:
            obs.update(message)

    def wakeAnimals(self):
        print("The ZooKeeper is waking up the animals.")
        self.notify("The Zookeeper is about to wake the animals!")
        for x in self.allAnimals:
            x.wakeUp()

    def rollCall(self):
        print("The ZooKeeper called roll.")
        self.notify("The Zookeeper is about to call roll!")
        for x in self.allAnimals:
            x.makeNoise()

    def feedAnimals(self):
        print("The ZooKeeper is feeding the animals.")
        self.notify("The Zookeeper is about to feed the animals!")
        for x in self.allAnimals:
            x.eat()

    def exerciseAnimals(self):
        print("The ZooKeeper is giving the animals exercises.")
        self.notify("The Zookeeper is about to exercise the animals!")
        for x in self.allAnimals:
            x.roam()

    def shutDown(self):
        print("The ZooKeeper is shutting down the zoo.")
        self.notify("The Zookeeper is about to close the zoo!")
        for x in self.allAnimals:
            x.sleep()


class ZooAnnouncer(Observer):
    def update(self, message):
        print("Hi, This is the Zoo Announcer. " + message)

# ----------- End of Observer Pattern ----------- #


# --------- main method
def main():
    Animals = []

    r1 = Rhino("Raakel")
    r2 = Rhino("Raini")
    Animals.append(r1)
    Animals.append(r2)

    h1 = Hippo("Henry")
    h2 = Hippo("Hector")
    Animals.append(h1)
    Animals.append(h2)

    e1 = Elephant("Ezra")
    e2 = Elephant("Evan")
    Animals.append(e1)
    Animals.append(e2)

    t1 = Tiger("Theodore")
    t2 = Tiger("Tucker")
    Animals.append(t1)
    Animals.append(t2)

    l1 = Lion("Liam")
    l2 = Lion("Leo")
    Animals.append(l1)
    Animals.append(l2)

    # ---- Cat delegation ----#
    c1 = Cat("Caleb")
    c1 = Concrete("Caleb")

    # Possible Behaviors
    behavior1 = ConcreteMewo("Caleb")
    behavior2 = ConcreteRun("Caleb")

    # Set behavior
    c1.setStrategy(behavior1)
    Animals.append(c1)

    c2 = Cat("Chloe")
    c2 = Concrete("Chloe")
    # Possible behavior
    behavior3 = ConcreteSleep("Chloe")
    c2.setStrategy(behavior3)
    Animals.append(c2)
    # ------------ We can change Cat's behavior in run-time ----------#

    w1 = Wolf("Wyatt")
    w2 = Wolf("Wade")
    Animals.append(w1)
    Animals.append(w2)

    d1 = Dog("Diego")
    d2 = Dog("Declan")
    Animals.append(d1)
    Animals.append(d2)

    # The ZooKeeper
    announcer = ZooAnnouncer()
    zoey = ZooKeeper(Animals)  # Pass list of animals to the Zookeeper
    zoey.register(announcer)  # Register observer "ZooAnnouncer"

    zoey.wakeAnimals()
    zoey.rollCall()
    zoey.feedAnimals()
    zoey.exerciseAnimals()
    zoey.shutDown()

    # zoey.remove(announcer) ----- To unregister an observer


if __name__ == '__main__':
    main()

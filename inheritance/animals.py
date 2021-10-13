from abc import abstractmethod


class Animal:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name + " is a " + self.get_type() + " and says " + self.speak()

    @abstractmethod
    def speak(self):
        pass

    @abstractmethod
    def get_type(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Woooof"

    def get_type(self):
        return "Dog"


class Cat(Animal):
    def speak(self):
        return "Mieow"

    def get_type(self):
        return "Cat"



d1 = Dog("Pluto")
print(d1)
c1 = Cat("Sylvester")
print(c1)


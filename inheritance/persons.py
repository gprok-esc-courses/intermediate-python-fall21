from abc import abstractmethod


class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    @abstractmethod
    def get_payment(self):
        pass


class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def get_payment(self):
        return self.salary

class Manager(Person):
    def __init__(self, name, salary, bonus):
        super().__init__(name)
        self.salary = salary
        self.bonus = bonus

    def get_payment(self):
        return self.salary + self.bonus


class HourlyWorker(Person):
    def __init__(self, name, hours, wage):
        super().__init__(name)
        self.hours = hours
        self.wage = wage

    def get_payment(self):
        return self.hours * self.wage

class ContractWorker(Person):
    def __init__(self, name, amount):
        super().__init__(name)
        self.amount = amount

    def get_payment(self):
        return self.amount + self.get_vat()

    def get_vat(self):
        return self.amount * 0.1

e = []
e.append(Employee("Nick", 800))
e.append(Employee("Peter", 1200))
e.append(Manager("Tom", 5000, 2500))
e.append(HourlyWorker("Jim", 30, 5))
e.append(ContractWorker("Mike", 6500))

# Payroll
for p in e:
    print(p.name + " payment:" + str(p.get_payment()))

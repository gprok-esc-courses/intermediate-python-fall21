from abc import abstractmethod
from factory import TransportationFactory

class PaymentStrategy:
    @abstractmethod
    def get_payment(self):
        pass


class Helicopter(PaymentStrategy):
    def get_payment(self):
        return 500


class Toll(PaymentStrategy):
    def get_payment(self):
        return 2.8


class PublicTransportation(PaymentStrategy):
    def get_payment(self):
        return 11.0


class Free(PaymentStrategy):
    def get_payment(self):
        return 0


class Taxi(PaymentStrategy):
    def get_payment(self):
        return 40.0


class Commute:
    def __init__(self):
        self.payment = None

    def calculate_cost(self):
        if self.payment is None:
            return 0
        else:
            return self.payment.get_payment()


if __name__ == '__main__':

    c = Commute()
    while True:
        transp_means = ['', 'Toll', 'Taxi', 'Public', 'Helicopter']
        print("1.Toll, 2.Taxi, 3.Public, 4.Hel, 0.Exit. Select: ")
        p = int(input())

        if p == 0:
            break
        c.payment = TransportationFactory.get_transportation(transp_means[p]).get_payment()

        print(c.calculate_cost())


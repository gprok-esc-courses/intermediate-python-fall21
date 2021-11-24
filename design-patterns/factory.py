from strategy import Taxi,Toll,PublicTransportation,Helicopter


class TransportationFactory:
    @staticmethod
    def get_transportation(type):
        if type == 'Toll':
            return Toll()
        elif type == 'Taxi':
            return Taxi()
        elif type == 'Public':
            return PublicTransportation()
        elif type == 'Helicopter':
            return Helicopter()
from uuid import uuid4


class Afto:
    """Avto xususiyatlar"""
    __nom_avto = 0

    def __init__(self, make, model, rang, yil, narh, km=0):
        """avtomobilning xususiyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narx = narh
        self.km = km
        self.__id = uuid4()
        Afto.__nom_avto += 1
    def __repr__(self):
        return f"{self.rang},{self.make},{self.model}"

avto1 = Afto("gm", "malibu", "black", 2020, 40000, 1000000)
print(avto1)


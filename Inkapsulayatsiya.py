from uuid import uuid4

class Avto:
    """Avtomobil classi"""
    __num_avto = 0
    def __init__(self,make,model,rang,yil,narh,km=0):
        """Avtomobil xususiyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        self.__km = km
        self.__id = uuid4()
        Avto.__num_avto += 1

    @classmethod
    def get_num_avto(cls):
        return cls.__num_avto

    def get_km(self):
        return self.__km

    def add_km(self,km):
        """Mashinaning km ga yana km qo'shihs"""
        if km >= 0:
            self.__km += km
        else:
            print("Mashinaning km kamaytirib bo'lmaydi")

    def get_id(self):
        return self.__id

avto1 = Avto("GM","malibu","qora",2020,40000,100000)
avto2 = Avto("GM","malibu","qora",2020,40000,100000)
avto3 = Avto("GM","malibu","qora",2020,40000,100000)
print(avto3.get_num_avto())
print(f"ID: {avto1.get_id()}")
print(f"KM: {avto1.get_km()}")
avto1.add_km(1500)
print(avto1.get_km())

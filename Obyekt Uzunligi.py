

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
        Avto.__num_avto += 1

class Avtosalon:
    """Avto salon classi"""
    def __init__(self,name):
        self.name = name
        self.avtolar = []

    def __repr__(self):
        return f"{self.name} avtosaloni"

    def add_avto(self,avto):
        if isinstance(avto, Avto):
            self.avtolar.append(avto)
        else:
            print("Avto Obyektini kiriting")

    def __len__(self):
        return len(self.avtolar)

salon1 = Avtosalon("MaxAvto")
# print(salon1)
avto1 = Avto("GM","Malibu","qora",2020,400000)
avto2 = Avto("GM","lacetti","qora",2020,200000)
avto3 = Avto("BMW","BMW","qora",2022,400000)

for avto in [avto1,avto2,avto3]:
    salon1.add_avto(avto)
print(len(salon1))




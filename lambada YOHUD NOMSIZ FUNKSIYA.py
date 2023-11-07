class Talaba:
    """Talaba nomli klass yaratamiz"""
    def __init__(self,ism,familiya,tyil):
        """Talabaning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.bosqich = 1

    def get_info(self):
        return f"{self.ism} {self.familiya}.{self.bosqich}-bosqich talabasi"

    def set_bosqich(self,bosqich):
        """Talabaning kursini yangilovchi metod"""
        self.bosqich = bosqich

    def update_bosqich(self):
        """Talabaning bosqichini 1 taga ko'paytiramiz"""
        self.bosqich += 1

talaba1 = Talaba("otabek","Ro'zmetov",2008)

talaba1.update_bosqich()
print(talaba1.get_info())

talaba1.update_bosqich()
print(talaba1.get_info())

class Talaba():
    def __init__ (self, familiya, ism, tyil):
        self.familiya = familiya
        self.ism = ism
        self.tyil = tyil
        # self.fakultet = fakultet
        # self.yonalish = yonalish
        # self.bosqich = bosqich
        # self.guruh = guruh
        # self.id = id

    def ism_familiyani_tyli(self):
        return f"Talabaning familiya ismi : {self.familiya} {self.ism} {self.tyil} tug'ulgan."

    def malumot(self):
        return f"Talaba {self.fakultet}da {self.yonalish}da o'qiydi."

    def kurusi_b_malumot(self):
        return f"Talaba {self.bosqich}-kurs {self.guruh} id raqami :{self.id}."


talaba1 = Talaba("Ro'zmetov", "Otabek", 2008, "uztelecom", "dasturlash", 2, 941_21, 9412203)
print(talaba1.malumot().title())


class Shaxs(Talaba):
    """Talaba klassi"""

    def __init__(self,familiya, ism, tyil, passport, idraqam):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, tyil)
        self.idraqam = idraqam


    def get_id(self):
        """Talabaning ID raqami"""
        return self.idraqam

    def get_fullname(self):
        fullname = f"Ismim {self.ism} familiya {self.familiya} "
        fullname += f"tyil {self.tyil}  id raqam {self.idraqam}"
        return fullname

inson = Shaxs("otabek","Ro'zmetov","KN55253",2008,121821)
print(inson.get_fullname())




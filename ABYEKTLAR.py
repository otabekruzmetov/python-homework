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

    def get_name(self):
        """Talabaning ismini qaytaradi"""
        return self.ism

    def get_lastname(self):
        """Talabaning familiyasini qaytaradi"""
        return self.familiya

    def get_fullname(self):
        """Talabaning ism-familiyasini qaytaradi"""

    def get_age(self,yil):
        """Talabaning yoshini qaytaradi"""
        return yil-self.tyil

    def get_name(self):
        """fan nomi"""
        return self.nomi

    def get_students(self):
        """fanga yozilgan talabalar haqida ma'lumot"""
        return [x.get_info()for x in self.talabalar]

    def get_students_num(self):
        """Fanga yozilgan talabalar soni"""
        return self.talabalar_soni


talaba1 = Talaba("otabek","Ro'zmetov",2008)
class Fan():
    def __init__(self,nomi):
        self.nomi = nomi
        self.talabalar_soni = 0
        self.talabalar = []

    def add_student(self,talaba):
        """Fanga talabalar qo'shish"""
        self.talabalar.append(talaba)
        self.talabalar_soni += 1

    def get_students(self):
        return [talaba.get_info()for talaba in self.talabalar]


# matematika = Fan("Oliy Matematika")
# talaba1 = Talaba("Otabek","Ro'zmetov",2008)
# talaba2 = Talaba("Behruz","Komiljanov",2008)
# talaba3 = Talaba("Jamshid","Iskandarov",2008)
#
# matematika.add_student(talaba1)
# matematika.add_student(talaba2)
# matematika.add_student(talaba3)

# print(matematika.talabalar_soni)

# print(matematika.talabalar)

# mat_talabalar = matematika.get_students()
# print(mat_talabalar)


# # print(talaba1.get_info())
# talaba1.bosqich= 2
# print(talaba1.bosqich)
# talaba1.set_bosqich(3)
# print(talaba1.get_info())



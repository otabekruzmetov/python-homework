# 'UY ISHI'
# '16-DARS FUNKSIYA'
# ('uyga vazifa sharti:"1.Foydalanuvchidan son olib, '
#  'uning kvadrati va kubini '
#  'konsolga chiqaruvchi funksiya yozing.')
#
# def Foydalanuvchi():
#     """Kvadrat va kubni konsolga chiqaruvchi funksiya"""
#     print(Foydalanuvchi.__doc__)
#     square = int(input("Hohlagan natural son yozing>>"))
#     print(f"{square} ning kavadrati, = {square,  2} ga teng")
#     print(f"{square} ning kubi, = {square,  3} ga teng")
#
# 'UY ISHI'
# "18-DARS FUNKSIYA VA RO'HAT"
# ("uyga vazifa sharti:Funkiyaga ro'yhat uzatib ro'yhatda "
#  "uchragan vali ismini birinchi harfini katta harf bilan,"
# "qolgan elementlarini hamma harfini katta harf bilan "
#  "chiqaring.Hamda ali ismli odamga salom yollang!")
#
#
# def katta_harf(matnlar):
#  for i in range(len(matnlar)):
#   matnlar[i] = matnlar[i].upper()
#   matnlar[1] = matnlar[1].title()
#
# ismlar = ['ali', 'vali', 'hasan', 'husan']
# katta_harf(ismlar)
# print(ismlar)
# print('salom ali'.title())
#
# def katta_harf(matnlar):
#     for i in range(len(matnlar)):
#         if matnlar[i] == 'ali':
#             matnlar[i] = matnlar[0].title()
#         else:
#             matnlar[i] = matnlar[i].upper()
#
#
# ismlar = ['ali', 'vali', 'hasan', 'husan']
# katta_harf(ismlar)
# print(ismlar)
#
# 'UY ISHI'
# '19-DARS Moslashuvchan funksiya'
# ('uyga vazifa sharti:"1.Istalgancha sonlarni qabul qilib, ularning'
#   "ko'paytmasini qaytaruvchi funksiya yozing")
#
# def sonlarni_qaytaravchi_funk(*sonlar):
#     """istalgan sonni qabul qilib ularning ko'paytmasini qaytaruvchi funksiya"""
#     yigindi = 1
#     for son in sonlar:
#         yigindi *= son
#     return yigindi
#
# print(sonlarni_qaytaravchi_funk.__doc__)
# print(sonlarni_qaytaravchi_funk(4, 5,6,2 ))
# print(sonlarni_qaytaravchi_funk(2,6))
#
#
#
# class Avto:
#     def __init__(self,rangi,nomi,model,narh,):
#         self.rangi =rangi
#         self.nomi = nomi
#         self.model = model
#         self.narh = narh
#         self.kilometr = 1800
#
#     def get_info(self):
#         return f"{self.rangi},{self.nomi}{self.model},{self.narh}{self.kilometr}"
#
#     def get_rangi(self):
#         """mashinani rangini qaytaruvchi"""
#         return self.rangi
#
#     def get_rangi(self):
#         """mashinani nomini qaytaruvchi"""
#         return self.nomi
#
#     def get_rangi(self):
#         """mashinani modelini qaytaruvchi"""
#         return self.model
#
#     def get_rangi(self):
#         """mashinani narhini qaytaruvchi"""
#         return self.narh
#
#     def kilometr(self,kilometr):
#         """mashinani km sini yangilovchi metod"""
#         self.kilometr = kilometr
#
#     def update_km(self):
#         """mashinani km sini qaytaruvchi"""
#         self.kilometr += 1
#
# avto1 = Avto("rangi""qora","nomi"   "bmw","m8","8000 000" )
# print(avto1.get_info().upper())
#
# avto1.update_km()
# print(avto1.get_info())
# avto1.update_km()
# print(avto1.get_info())



# "UY ISHI"
# """26-DARS UYGA VAZIFA SHARTI:"""
#
# class Foydalanuvchi:
#     def __init__(self,ism,familiya,tyil,username):
#         """Foydalanuvchi haqida malumot"""
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
#         self.username = username
#
#     def get_fullname(self):
#         """Foydalanuvchi haqida malumoti"""
#         fullname = f"{self.ism} {self.familiya},"
#         fullname += f"{self.tyil} {self.username}"
#         return fullname
#
#     def age_yil(self,yil):
#         """Foydalanuvchini yoshini qaytaruvchi metod"""
#         return yil - self.tyil
#
# user = Foydalanuvchi("Otabek","Ro'zmetov",2008,"otabek12")
# print(f"{user.get_fullname()}, {user.age_yil(2023)} yoshda")
#
# class Admin(Foydalanuvchi):
#     """admin voris class"""
#     def __init__(self,ism,familiya,tyil,username):
#         """Admin xususiyatlari"""
#         super().__init__(self,ism,familiya,tyil,username)
#
#     def ban_user(self,user):
#         """user"""
# print(f"Foydalanuvchi {user.ism} {user.familiya} bloklandi")


"UY ISHI"
from uuid import uuid4


class Shaxs:
    """Shaxslar haqida ma'lumot"""

    def __init__(self, ism, familiya, passport, tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil

    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f" Passport: {self.passport}, {self.tyil}-yilda tug`ilgan"
        return info

    def get_age(self, yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil - self.tyil


class Talaba(Shaxs):
    """Talaba klassi"""

    __talaba_soni = 0

    def __init__(self, ism, familiya, passport, tyil):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.__id = uuid4()
        self.bosqich = 1
        Talaba.__talaba_soni += 1

    @classmethod
    def get_talabalarsoni(cls):
        return f"Talabalar soni:{cls.__talaba_soni}"

    def get_id(self):
        """Talabaning ID raqami"""
        return self.__id

    def get_bosqich(self):
        """Talabaning o'qish bosqichi"""
        return self.bosqich

    def get_info(self):
        """Talaba haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.__id}"
        return info


Talaba1 = Talaba(f"Otabek", "Ro'zmetov", "adAd", 2009, )
Talaba2 = Talaba(f"Azizbek", "Alimov", "aaa242", 2001, )
Talaba3 = Talaba(f"Fazliddin", "Dabuluov", "adsdaa242", 2005)
Talaba4 = Talaba(f"Lziz", "Raxmonov", "aaa242", 2008, )
print(Talaba1.get_talabalarsoni())
print(Talaba1.get_info())
print(Talaba2.get_info())
print(Talaba3.get_info())
print(Talaba4.get_info())







def salom_ber():
    """Salom beruvchi funksiya"""
    print('Asalomu alykum')

salom_ber()

def salom_berayapti(ism):
    """Foydalanuvchi ismini qabul qilib, unga alom beruvchi funksiya"""
    print(f"Asalomu alykum, hurmatli {ism.upper()}!")
print(salom_berayapti.__doc__)
salom_berayapti('otabek')
salom_berayapti('jahongir')
salom_berayapti('olim')
salom_berayapti('sarvar')

def toliq_ism(ism,familiya):
    """Foydalanuchi ism va familiyasini jamlab chiqaruvchi funksiya"""
    print(f"Foydalanuvchi ism: {ism.title()}\n"
          f"Foydalanuvchi familiyasi: {familiya.title()}")
print(toliq_ism.__doc__)
toliq_ism('olim','hakimov')

def yosh_hisobla(tugilgan_yil,joriy_yil=2022):
    """Foydealanuvchi tug'ilgan yilidan unung yoshini hisoblaydi"""
    print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")
yosh_hisobla(1995,2020)
yosh_hisobla(1993)

def ism_fam(ism='otabek',fam='rozmetov'):
    """Ism va familiyani chiqaruvchi funksiya"""
    print(f"Foydalanuvchi ism: {ism.title()}\n"
          f"Foydalanuvchi familiyasi: {fam.title()}")
ism_fam()






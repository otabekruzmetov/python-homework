'UY ISHI'
'16-DARS FUNKSIYA'
('uyga vazifa sharti:"1.Foydalanuvchidan son olib, '
 'uning kvadrati va kubini '
 'konsolga chiqaruvchi funksiya yozing.')

def Foydalanuvchi():
    """Kvadrat va kubni konsolga chiqaruvchi funksiya"""
    print(Foydalanuvchi.__doc__)
    square = int(input("Hohlagan natural son yozing>>"))
    print(f"{square} ning kavadrati, = {square,  2} ga teng")
    print(f"{square} ning kubi, = {square,  3} ga teng")

'UY ISHI'
"18-DARS FUNKSIYA VA RO'HAT"
("uyga vazifa sharti:Funkiyaga ro'yhat uzatib ro'yhatda "
 "uchragan vali ismini birinchi harfini katta harf bilan," 
"qolgan elementlarini hamma harfini katta harf bilan "
 "chiqaring.Hamda ali ismli odamga salom yollang!")


def katta_harf(matnlar):
 for i in range(len(matnlar)):
  matnlar[i] = matnlar[i].upper()
  matnlar[1] = matnlar[1].title()

ismlar = ['ali', 'vali', 'hasan', 'husan']
katta_harf(ismlar)
print(ismlar)
print('salom ali')
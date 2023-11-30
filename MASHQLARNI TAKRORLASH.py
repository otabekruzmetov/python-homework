# ism = "Otabek"
# yosh = 15
# print(ism)
# print(yosh)

# ism = "otabek"
# print(ism)
# ism="temur"
# print(ism)
#foydalanuvchining tug'ilgan yilini so'raymiz
# t_yil = input("Tug'ilgan yilingizni kiriting: ")
# yosh = 2023 - t_yil #
# print("Siz " + yosh + " yoshda ekansiz")
#
# shahar = "Urganch"
# viloyat = "Xorazm"
# #
# ism = "Otabek"
# familiya = "Ro'zmetov"
# print(ism + familiya)
# #
# ism = ['otabek','umid','ali','vali']
# ism.append('murot')
# ism = input(' Hohlagan ism tanglang')
# print("siz tanlagan ism ro'yhatimizda bor")
# print(ism)

# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"] # mevalar ro'yxati (matnlar)
# narhlar = [12000, 18000, 10900, 22000] # narhlar ro'yxati (sonlar)
# sonlar = ['bir', 'ikki', 3, 4, 5] # sonlar va matnlar aralash ro'yxat
# ismlar = [] # bo'sh ro'yxat
# print(mevalar)
# print(narhlar)

# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"] # mevalar ro'yxati (matnlar)
# print("Birinchi meva: ", mevalar[0])
# print("Ikkinchi meva: ", mevalar[1])

# ismlar = ['otabek','kamron','sanjar','javohir']
# print("birinchi ism: ", ismlar[1])
# print("ikkinchi ismlar: ", ismlar[3])
#
# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"] # mevalar ro'yxati (matnlar)
# print(mevalar)
# print("Birinchi meva: ", mevalar[0].title())
# print("Ikkinchi meva: ", mevalar[1].upper())

# narhlar = [12000,18000,10900,22000]
# print(narhlar[2] + narhlar[3])

# narhlar = [12000,18000,10900,22000]
# narhlar[0]=13000
# narhlar[2]=11000
# narhlar[3]=narhlar[3]+200
# print(narhlar)

# mmehmonlar = ['jonibek','temur','javlon','otabek']
# for mehmon in mehmonlar:
#     print(mehmonlar)

# mehmonlar = ['jonibek','temur','javlon','otabek']
# for mehmon in mehmonlar:
#     print(f"Hurmatli {mehmon},sizni 20-mart kuni oshga taklif qiilamiz")
#     print("Hurmat ila Ro'zmetov")

# mehmonlar = ['Jonibek', 'Temurbek', 'Javlonbek', 'O\’tkirbek']
# for mehmon in mehmonlar:
#     print(mehmon)
#
# print(mehmonlar)  # bu qator tsikl tashqarisida bo'lishi kerak edi
#
# sonlar = list(range(1,11))
# for son in sonlar:
# #     print(f"{son} ning kvadrati0{son**2} ga teng")
#
# sonlar = list(range(11))
# for son in sonlar:
#     sonlar_kvadrati.append(son**2)
#     print('sonlar')
#     print('sonlar_kvadrati')

# dostlar = []
# print("5 ta yaqin do'stingiz kim?")
# for n in range(5):
#     dostlar.append(input(f"{n+1} dostingiz ismini kiriting:"))
#     print(dostlar)

# mehmonlar = ['Jonibek', 'Temurbek', 'Javlonbek', 'O\’tkirbek', 'Anvar', 'Bekzod']
# print("sorted() qaytargan ro'yxat:", sorted(mehmonlar))
# print("Asl ro'yxat o'zgarmas qoldi:", mehmonlar)


# dasturchilar = {
#     'ali':['python','c++'],
#     'vali':['html','css','js'],
#     'hasan':['php','sql'],
#     'husan':['python','php'],
#     'maryam':['c++','c#']
#     }
#
# for ism, tillar in dasturchilar.items():
#     print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:")
#     for til in tillar:
#         print(til.upper())

# mevalar = ['olma','anjir','anor','shaftoli']
# mevalar.append('tarvuz')
# print(mevalar)
#
# cars = []
# cars.append('lacetti')
# cars.append('nexia 3')
# cars.append('cobalt')
# print(cars)

# cars = ['lacetti','nexia3','cobalt']
# cars.insert(2,'malibu')
# print(cars)
# cars.insert(2, 'Damas') # 3-o'ringa yangi qiymat qo'shamiz
# # print(cars)
# mavalar = ['olma','ajir','shaftoli',"o'rik",'anor']
# # del mavalar[1]
# # print(mavalar)
# mevalar = ['olma','anor','anlir','shaftoli']
# mevalar.remove('shaftoli')
# print(mevalar)
# bozorlik = ['olma',"yog'",'un',"go'sht","saryog'"'banan']
# mahsulot=bozorlik.pop(3)
# print("men " + mahsulot +" sotib oldim")
# print("olinmagan mahsulotlar:",bozorlik)
#
# mevalar = ['olma','anor','anjir','shaftoli']
# print("Birinchi meva",mevalar[0].title())
# print("Ikkinchi meva",mevalar[3].upper())
#
# sonlar = [1200,1400,1500,1600]
# # print(sonlar[1]+sonlar[2])
# sonlar[0]=1300
# sonlar[2]=1900
# sonlar[3]=sonlar[3]+1500
# print(sonlar)

# import random
#
# random_telefon_raqam = []
# ishora = True
# while ishora:
#     tel = random_telefon_raqam.append(input(f" Telefon raqamingzni kiriting>> +{998} "))
#     savol = input("Yana tel kiritasizmi (ha/yo'q)")
#     if savol.lower() == 'ha':
#         continue
#     else:
#         ishora = False
#     if (input("STRART tugmasini bosing>>")).lower() == 'start':
#         telefon_raqam = random.choice(random_telefon_raqam)
#         print(f"{telefon_raqam} - siz yutdingz, sizni omad showda kutamiz")
#     else:
#         print("YANA START TUGMASINI BOSIB KURING KURING")

# cars = ['bmw','mers','general motoros','tesla','volvo','audi']
# cars.sort()
# print(cars)
#
# mehmonlar = ['Jonibek', 'Temurbek', 'Javlonbek', 'O\’tkirbek', 'Anvar', 'Bekzod']
# print("sorted() qaytargan ro'yxat:", sorted(mehmonlar))
# print("Asl ro'yxat o'zgarmas qoldi:", mehmonlar)

# mehmonlar = ['olloh',"payg'ambar",'sahobalar',"hazrati Ali"]
# mehmonlar.append('abu abkir')
# mehmonlar.__len__()
# print(mehmonlar.remove() = True)
# print(mehmonlar)

# mehmonlar = ['otabek','sanjar','javohir','akmal']
# for mehmon in mehmonlar:
    # print(mehmon)
#
# mehmonlar = ['otabek','sanjar','javohir','akmal']
# for mehmon in mehmonlar:
#     print(f"Hurmatli {mehmon} sizni uyga taklif qilamiz")

# mehmonlar = ['otabek','sanjar','javohir','akmal']
# for mehmon in mehmonlar:
    # print(mehmon)

# print(mehmonlar)
#
# sonlar = list(range(1,11))
# for son in sonlar:
#     print(f"{son} ning kvdrt {son**2} ga teng")
#
# son = 1
# while son <= 5:
#     print(son,end='')
#     son = son + 1
#
# print("Kiritilgan sonning kvadratini qaytaruvchi dastur")
# savol = "Istalgan son kiriting"
# savol += "(dasturni to'xtatish uchun exit deb yozing):"
# qiymat = ""
# while qiymat !='exit':
#     qiymat = input(savol)
#     if qiymat != "exit":
#         print(float(qiymat)**2)
# print("istalgan ismni tanglang")
# variatlar1 = ['otabek','jasutr','sanjar']
# print(variatlar1)
# variatlar = "(Dasturnio to'xatamoqchi bo'lsangiz stop deb yozing):"
# ism = ''
# while ism != 'stop':
#     ism = input(variatlar)
#     if ism !="stop":
#         print(str(ism))
#
# ismlar = ['ali','umar''zubayir','abubakr','usmon','said abu vaqos','abdurahmon']
# ismlar.append('ALLOH')
# ismlar.sort()
# print(ismlar)

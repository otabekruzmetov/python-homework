# talaba_0 = {
#     'ism':'otabek',
#     'familiya':'rozmetov',
#     'yosh':15,
#     'fakultet':'kompyuter injenering',
#     'kurs':2
# }
# for kalit, qiymat in talaba_0.items():
#     print(f"Kalit: {kalit}")
#     print(f"{qiymat} \n")
#
# telefonlar = {
#     'ali':'iphone x',
#     'vali':'samsung a10 ',
#     'olim':'mi 10pro',
#     'orif':'nokia 3310',
# }
#
# for k, q in telefonlar.items():
#     print(f"{k.title()}ning telefoni {q}")
#
# mahsulotlar = {
#     'olma':10000,
#     'anor':20000,
#     'uzum':30000,
#     'anjir':40000,
#     'shaftoli':50000,
# }
# bozorlik = ['anor', 'uzum', 'non', 'baliq']
# # for mahsulot in mahsulotlar:
# #     if mahsulot in bozorlik:
#
# #         print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")
# # for buyum in  bozorlik:
# #     if buyum not in mahsulotlar:
# #         print(f"Iltimos, do'koningizga {buyum} ham olib keling")
#
# # print(mahsulotlar.keys())
# # print("do'kondagi mahsulotlar:")
# # for mahsulot in mahsulotlar.keys():
# #     print(mahsulot.title())
#
# print("Do'konimizdaagi mahsulotlar:")
# for mahsulot in sorted(mahsulotlar):
#     print(mahsulot.title())

# telefonlar = {
#     'ali':'iphone x',
#     'vali':'samsung a10 ',
#     'olim':'mi 10pro',
#     'orif':'nokia 3310',
#     'umar':'nokia 3310',
#     'ali':'samsung a10',
#     'farida':'samsung a10'
# }
#
#
# print(telefonlar.values())
# print(f"Foydalanuvchilar quyidagi telefonlarni ishlatadilar")
# for tel in  set(telefonlar.values()):
#     print(tel)

# Pyhyton = {
#     'Bekmurod': 'lavash',
#     'Temur':'palov',
#     'Shoxrux': 'shaverma',
#     'Odil': 'manti',
#     'Kamoron': 'shurpa',
#     'Laziz': 'norin',
#     'Hamid': 'shashlik',
#     'Hurmat':'osh',
#     'Aiz':'barak',
#     'Nemat':'galupsi'
# }
# print(Pyhyton.items())
#
# for kalit,qiymat in Pyhyton.items():
#     print(f"{kalit} - {qiymat.title()}")
#1.

#

#
Davlatlar={
    "o'zbekiston":"toshkent",
    "aqsh":"washington",
    "italia":"rim",
    'rassiya':'maskva',
    'qozoqiston':'bishkek',
}
print('Dunyo davlatlari:')
for davlat in sorted(Davlatlar):
    print(davlat.upper())

print('\nDavlatlarning poytaxtlari')
for poytaxt in sorted(Davlatlar.values()):
    print(poytaxt.title())


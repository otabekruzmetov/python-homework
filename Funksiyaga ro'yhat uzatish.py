# def bahola(ismlar):
#     baholar = {}
#     while ismlar:
#         ism = ismlar.pop()
#         baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
#         baholar[ism]=baho
#     return baholar
#
talabalar = ['ali','vali','hasan','husan']
# baholar = bahola(talabalar)
# print(talabalar)

#
# def katta_harf(matnlar):
#     matnlar = matnlar[:]
#     for i in range(len(matnlar)):
#         matnlar[i]=matnlar[i].title()
#     return matnlar
# ismlar = ['ali','vali','hasan','husan']
# yangi_ismlar = katta_harf(ismlar)
# print(ismlar)
# print(yangi_ismlar)

# talabar = ['ali','vali','hasan','husan']

# def bahola(ismlar):
#     baholar = {}
#     for ism in ismlar:
#         baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
#         baholar[ism] = baho
#         return baholar
#
# baholar = bahola(talabalar)
# print(baholar)
# print(talabalar)
#
# def katta_harf(matnlar):
#     matnlar = matnlar[:]
#     for i in range(len(matnlar)):
#         matnlar[i]=matnlar[i].title()
#     return matnlar
# ismlar = ['ali','vali','hasan','husan']
# yangi_ismlar = katta_harf(ismlar)
# print(ismlar)
# print(yangi_ismlar)

# def katta_harf(matnlar):
#     for i in range(len(matnlar)):
#         matnlar[i] = matnlar[i].upper()
#         matnlar[0] = matnlar[0].title()
#
#
# ismlar = ['ali', 'vali', 'hasan', 'husan']
# katta_harf(ismlar)
# print(ismlar)

# def katta_harf(matnlar):
#    for i in range(len(matnlar)):
#        matnlar[i]=matnlar[i].title()
# ismlar = ['ali', 'vali', 'hasan', 'husan']
# katta_harf(ismlar)
# print(ismlar)

def katta_harf(matnlar):
    for i in range(len(matnlar)):
        matnlar[i]=matnlar[i].upper()
        matnlar[1]=matnlar[1].title()
ismlar = ['ali','vali','hasan','husan']
katta_harf(ismlar)
print(ismlar)
print('salom ali')
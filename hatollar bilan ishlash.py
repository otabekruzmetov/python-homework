# yosh = input("Yoshingizni kiriting")
# try:
#     yosh = int(yosh)
#
# except:
#     print("Butun son kirirting")
# else:
#     print(f"Siz {2023 - yosh} yilda tug'ilgansiz")

# yosh = input("Yoshingizni kiriting")
# try:
#     yosh = int(yosh)
# except ValueError:
#     print("Butun son kirititmadingiz")
# else:
#     print(f"Siz {2023 - yosh} yilda tug'ilgansiz")

# x,y = 5,10
# try:
#     y/(x-5)
# except ZeroDivisionError:
#     print("0 bo'lib bolmaydi")

# mevalar = ['olma','anor','najir','uzum']
# try:
#     print(mevalar[7])
# except IndexError:
#     print(f"Ro'yxatda {len(mevalar)} ta meva bor xolos")
#
# user = {"username":"otabek",
#         "status":"admin",
#         "email":"otabek12182gmail.com",
#         "phone":"998886001218"}
#
#
# key="tel"
# try:
#     print(f'Foydalanuvchi: {user[key]}')
# except KeyError:
#     print("Bunday kalit mavjud emas")

# filename = "data.txt"
# with open(filename) as f:
#     text = f.read()

# son = input("Butun son kiriting: ")
# try:
#     son = int(son)
#     x=20/son
# except ValueError: # agar foydalanuvchi butun son kiritmasa
#     print("Butun son kiritmadingiz")
# except ZeroDivisionError: # agar foydalanuvchi 0 kiritsa
#     print("0 ga bo'lib bo'lmaydi")
# else:
#     print(f"x={x}")
#
# son = input("butun son kiriting")
# try:
#     son = int(son)
#     x=20/son
# except ValueError:
#     print("Butun son kiirtmadingiz")
# except ZeroDivisionError:
#     print("0 ga bo'lib bolmaydi")
# else:
#     print(f"x={x}")

# import json
# files = ['talaba1.json','talaba2.json','talaba3.json','talaba4.json']
# for filename in files:
#     try:
#         with open(filename) as f:
#             talaba = json.load(f)
#     except FileNotFoundError:
#         print(f"{filename} mavjud emas")
#     else:
#         print(talaba['ism'])
#         # fayl ustida turli amallar
# import json
# files=['talaba1.json','talaba2.json','talaba3.json','talaba4.json']
# for filename in files:
#     try:
#         with open(filename) as f:
#             talaba = json.load(f)
#     except FileNotFoundError:
#         pass
#     else:
#         print(talaba['ism'])

# while True:
#     yosh = input("Yoshingizni kiriting: ")
#     if yosh.isdigit():
#         yosh = int(yosh)
#         break
#
# print(f"Siz {2023-yosh} yilda tug'ilgansiz")

while True:
    yosh = input("yoshingizni kiritring")
    if yosh.isdigit():
        yosh = int(yosh)
        break

print(f"siz {2023-yosh} yilda tug'ilgansiz")





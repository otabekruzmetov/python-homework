# filename = 'server.txt'
# with open(filename) as file:
#     server = file.readlines()
# server = [server.rstrip() for server in server]
#
# print(server)
#
# faylnomi = 'server.txt'
# with open(faylnomi,'w') as fayl:
#     fayl.write('otabek rozmetov')

# faylnomi = 'new_file.txt'
# with open(faylnomi,'a') as fayl:
#     fayl.write("\nOtabek Ro'zmetov".upper())
#     fayl.write("2008")
#
#
# import pickle
#
# talaba1 = {'ism':'otabek','familiya':"ro'zmetov","tyil":2008}
# talaba2 = {'ism':"og'abek",'familiya':"ro'zmetov","tyil":2008}
#
# with open('info','wb') as file:
#     pickle.dump(talaba1,file)
#     pickle.dump(talaba2,file)
#
# with open('info','rb') as file:
#     talaba1 = pickle.load(file)
#     talaba2 = pickle.load(file)
#
# print(talaba1)
# print(talaba2)


"""Quyidagi pi_million_digits.txt faylini yuklab oling (faylda   soni nuqtadan so'ng million xona aniqlik bilan yozilgan).
Sizning tug'ilgan kuningiz  soni tarkibida uchraydimi yoki yo'q ekanligini aniqlovchi funksiya
yozing. Misol uchun, tug'ilgan sanangiz 25 Fevral, 2000-yil bo'lsa, 25022000 ketma-ketligi yuqoridagi
 matnda uchraydimi yo'q toping.
Fayl ichidagi matnni float ma'lumot turiga o'tkazing va pickle yordamida yangi faylga saqlang."""

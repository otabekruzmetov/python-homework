# import math
# uzunlik = lambda pi,r:2*pi*r
# print(uzunlik(math.pi,10))

# def daraja(n):
    # return lambda x : x**n

# kvadarat = daraja(2)
# kub = daraja(3)
# print(f"3-ning kvadrati {kvadarat(3)} ga, kubi esa {kub(3)} ga teng")
#
# from math import sqrt
#
# sonlar = list(range(11))
# ildizlar = list(map(sqrt,sonlar))
#
# print(ildizlar)

sonlar = list(range(11))

# def daraja2(x):
    # """Berilgan sonning kvadrati qaytaruvchi funksiya"""
    # return x*x
# print(daraja2.__doc__)
# print(list(map(daraja2,sonlar)))
# kvadratlar = list(map(lambda x:x,sonlar))
# print(kvadratlar)

kvadratlar = []
for son in  sonlar:
    kvadratlar.append(son*son)
print(kvadratlar)

a = [4,5,6]
b = [7,8,9]
a_plus_b = list(map(lambda x,y:x+y,a,b))
print(a_plus_b)
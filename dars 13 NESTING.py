car0 = {
    'model': 'lacetti',
    'rang': 'oq',
    'yil': 2018,
    'narh': 13000,
    'km': 50000,
    'korobka': 'avtomat'
}

car1 = {
    'model': 'nexia 3',
    'rang': 'qora',
    'yil': 2015,
    'narh': 9000,
    'km': 890000,
    'korobka': 'mexanika'
}

car2 = {
    'model': 'gentra',
    'rang': 'qizil',
    'yil': 2015,
    'narh': 9000,
    'km': 890000,
    'korobka': 'mexanika'
}

car = car0
print(f"{car['model'].title()},\
    {car['rang']} rang,\
    {car['yil']}-yil, {car['narh']}$")

car = car1
print(f"{car['model'].title()},\
    {car['rang']} rang,\
    {car['yil']}-yil, {car['narh']}$")

# car = car2
print(f"{car['model'].title()},\
    {car['rang']} rang,\
    {car['yil']}-yil, {car['narh']}$")

cars = [car0,car1,car2]
for car in cars:
    print(f"{car['model'].title()},\
{car['rang']} rang,\
{car['yil']}-yil, {car['narh']}$")
print(cars[0])
print(cars[0]['model'])
print(f"{cars[2]['rang'].title()}"
      f"{cars[2]['model']}")

malibus = []
for n in range(10):
    new_car = {
        'model':'malibu',
        'rang':None,
        'yil':2020,
        'narh':None,
        'km':0,
        'korobka':'avto'
    }
    malibus.append(new_car)
# print(malibus)
for malibu in malibus[:3]:
    malibu['rang']='qizil'
for malibu in malibus[3:6]:
    malibu['rang']='qora'
    # print(malibus)
for malibu in malibus:
    if malibu['korobka']=='avto':
        malibu['narh']=40000
    else:
        malibu['narh']=35000
print(malibus)

hamkasblar = {
    'ali':{'fanmiliya':'valiyev',
           'tyil':1995,
           'malumot':'oliy',
           'tillar':['python','c++']
            },

    'vali':{'fanmiliya':'aliyev',
           'tyil':2001,
           'malumot':'orta maxsus',
           'tillar':['html','css','js']
            },
    'hasan':{'fanmiliya':'husanov',
           'tyil':1999,
           'malumot':'maxsus',
           'tillar':['python','php']
},
}
for ism, info in hamkasblar.items():
    print(f"\n{ism.title()} {info['familiya'].title()}, "
          f"{info['tyil']}-yilda tug'ilgan. "
          f"Ma'lumoti: {info['malumot']}. \n"
          "Quyidagi dasturlash tillarini biladi:")
    for til in info['tillar']:
        print(til.upper())
print(hamkasblar)

ajdodlar = {
    'ism':'Abu Abdullox Muhammad ibn Ismoil',
    'tavalud topgan yeri':'Buxoro',
    'tuglgan sanasi':810,
    'necha yil umr korgan':60,
}
print(ajdodlar)

ajdodlar = {
    'ism':'Abdula Qodiriy',
    'tavalud topgan yeri':'Toshkent',
    'tuglgan sanasi':1849,
    'necha yil umr korgan':44,
}
print(ajdodlar)

ajdodlar = {
    'ism':'Erkin Vohidov',
    'tavalud topgan yeri':'fargona',
    'tuglgan sanasi':1936,
    'necha yil umr korgan':80,
}
print(ajdodlar)

ajdodlar = {
    'ism':'Alisher Navoiy',
    'tavalud topgan yeri':'Xirotdea',
    'tuglgan sanasi':1441,
    'necha yil umr korgan':60,
}

ajdodlar = [
     {
    'ism':['Abu Abdullox Muhammad ibn Ismoil'],
    'tavalud topgan yeri':['Buxoro'],
    'tuglgan sanasi':[810],
    'necha yil umr korgan':[60],
     },
     {
    'ism':['Abdula Qodiriy'],
    'tavalud topgan yeri':['Toshkent'],
    'tuglgan sanasi':[1849],
    'necha yil umr korgan':[44],
     },
     {
    'ism':['Erkin Vohidov'],
    'tavalud topgan yeri':['fargona'],
    'tuglgan sanasi':[1936],
    'necha yil umr korgan':[80],
     },
     {
    'ism':['Alisher Navoiy'],
    'tavalud topgan yeri':['Xirotdea'],
    'tuglgan sanasi':[1441],
    'necha yil umr korgan':[60],
     },]
for malumot in ajdodlar:
    print(f"\n{ajdodlar} Ajdodlaramiz haqida malumotlar")
for malumot in ajdodlar:
    print(ajdodlar)

    buxoriy = {'ism': 'Abu Abdulloh Muhammad ibn Ismoil',
               'tyil': 810,
               'vyil': 870,
               'tjoy': 'Buxoro'
               }

    qodiriy = {'ism': 'Abdulla Qodiriy',
               'tyil': 1894,
               'vyil': 1938,
               'tjoy': 'Toshkent'
               }

    vohidov = {'ism': 'Erkin Vohidov',
               'tyil': 1936,
               'vyil': 2016,
               'tjoy': "Farg'ona"
               }

    navoiy = {'ism': 'Alisher Navoiy',
              'tyil': 1441,
              'vyil': 1501,
              'tjoy': "Xirot"
              }

    shaxslar = [buxoriy, qodiriy, vohidov, navoiy]

    for shaxs in shaxslar:
        ism = shaxs['ism']
        tyil = shaxs['tyil']
        vyil = shaxs['vyil']
        tjoy = shaxs['tjoy']
        print(f"{ism} {tyil}-yilda {tjoy}da tavallud topgan. "
              f"{vyil - tyil} yil umr ko'rgan.")




def katta_harf(matnlar):
    for i in range(len(matnlar)):
        if matnlar[i] == 'ali':
            matnlar[i] = matnlar[0].title()
        else:
            matnlar[i] = matnlar[i].upper()
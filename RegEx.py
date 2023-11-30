# import re
# matn = """Maqolalar  2023-yilning 20-martiga qadar jonibekdev@gmail.com elektron pochtasida qabul qilinadi.
# Quyidagi yo'nalishdagi maqolalar qabul qilinadi:
# 👉 Aniq va tabiiy fanlarni zamonaviy pedagogik texnologiyalar asosida o‘qitish  metodikasi.
# 👉 Umumta’lim  fanlarini o‘qitishda  STEAM yondashuvning o’rni va ahamiyati. """

# andoza = '[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'
# email = re.findall(andoza,matn)


import re
matn = "Mening ismim Bahodir. Yoshim 15 da. Veb manxilim: https://github.com/ilyushaparen.com Bu githunb manzil."
tekshiruvchi = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*|\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
tekshirish = re.findall(tekshiruvchi,matn)
print(tekshirish)


with open("web_manzi.txt", 'w+') as file:
    for address in tekshirish:
        file.write(address)
    


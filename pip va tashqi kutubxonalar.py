from googletrans import Translator
#
# tarjimon = Translator()
# matn_uz = "Python - dunyodagi eng mashxur daasturlash tili "
# tarjimon = tarjimon.translate(matn_uz, dest='ru')
# print(tarjimon.text)

# import requests
# from pprint import pprint
#
# manzil= "https://kun.uz/news/main"
# r = requests.get(manzil)
# pprint(r.text)

# import requests
# API_KEY = '06e67e7830a22889722ff843'
# birlik='USD'
# url =f"https://v6.exchangerateapi.com/v6/{API_KEY}/pair/{birlik}/UZS"
# response = requests.get(url)
# kurs = response.json()['conversion_rate']
# print(kurs)
# #
# import requests
# from bs4 import BeautifulSoup
#
# sahifa = "https://kun.uz/news/main"
# r = requests.get(sahifa)
#
#
# soup = BeautifulSoup(r.text, 'html.parser')
# news = soup.find_all(class_="news-title") # yangiliklarning mavzusini ajratib olamiz
# print(news[0].text) # eng birinchi yangilikni konsolga chiqaramiz

# import requests
#
# from bs4 import BeautifulSoup
# from wordcloud import WordCloud
# import matplotlib.pyplot as plt
#
# sahifa = "https://kun.uz/news/main"
# r = requests.get(sahifa)
#
# soup = BeautifulSoup(r.text, 'html.parser')
# news = soup.find_all(class_="news-title")
# matn = ""
# for n in news:
#     matn += n.text
#
# # kerakmas so'zlar
# stopwords = ["учун", "бўйича", "лекин", "билан", "ва", "бор", "ҳам", "хил", "йил"]
# # bulutni yaratamiz
# wordcloud = WordCloud(width=1000, height=1000,
#                       background_color='white',
#                       stopwords=stopwords,
#                       min_font_size=20).generate(matn)
#
# # plot the WordCloud image
# plt.figure(figsize=(8, 8), facecolor=None)
# plt.imshow(wordcloud)
# plt.axis("off")
# plt.tight_layout(pad=0)
# plt.show

# import requests
# from pprint import pprint as print
#
# API_KEY = '5796872f7a1038c6cbf7c65f'
#
# currency='USD'
# url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{currency}/UZS"
# response = requests.get(url)
# kurs = response.json()['conversion_rate']
# print(f"1 dollar kursi {kurs} so'mga teng")

# from fuzzywuzzy import fuzz

# print(fuzz.ratio("salom","assalom"))
# print(fuzz.ratio("salom","salim"))

# from fuzzywuzzy import process
# from uzwords import words
# text = "салом"
# matches = process.extract(text, words, limit=3 )
# print(matches)

import cv2

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 5)
        roi_gray = gray[y:y+w, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 5)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# copyright Tim Ruscia aka techwithtim
# code from

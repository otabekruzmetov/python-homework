import json
#
# filname = 'data.json'
# with open(filname) as f:
#     data = json.load(f)
#
# kenglik = data['geometry']['location']['lat']
# uzunlik = data['geometry']['location']['lag']
# print(f"{kenglik},{uzunlik}")

# x = 10
# x_json = json.dumps
#
# ism = "Oatbek"
# ism_json = json.dumps(ism)
# print(ism_json)
#
# sonlar = [12,15,18,67]
# sonlar_json = json.dumps(sonlar)
# print(sonlar_json)
# print(type(sonlar_json))
#
# bemor = {
#     "ism":"Otabek Ro'zmetov",
#     "yosh":30,
#     "oil":True,
#     "farzandlari":("ali","fotima"),
#     "allergiya":None,
#     "dorilar":[
#         {"nomi":"Analgin","miqdori":0.5},
#         {"nomi":"Panadol","miqdori":0.5}
#     ]
# }
# bemor_json = json.dumps(bemor,indent=5)
# print(bemor_json)
#
# bemor = {
#     "ism":"Otabek Ro'zmetov",
#     "yosh":30,
#     "oil":True,
#     "farzandlari":("ali","fotima"),
#     "allergiya":None,
#     "dorilar":[
#         {"nomi":"Analgin","miqdori":0.5},
#         {"nomi":"Panadol","miqdori":0.5}
#     ]
# }
with open('bemor.json','w') as f:
    json.dump(bemor,f)


import json
filname = 'data.json'
with open(filname) as f:
    data = json.load(f)

kenglik = data['geometry']['location']['lat']
uzunlik = data['geometry']['location']['lng']
print(f"{kenglik} {uzunlik}")
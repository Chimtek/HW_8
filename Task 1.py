import requests

heroes_id = ('332', '149', '655', '53', '212', '445', '566')
heroes_data = {}
for id in heroes_id:
    url = f'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/id/{id}.json'
    req = requests.get(url)
    heroes_data[req.json()['name']] = req.json()['powerstats']['intelligence']

for hero, intel in heroes_data.items():
    print(f'Герой: {hero}, умственный коэффициент: {intel}')

print('-' * 50)
print(f'Самый умный из списка - {max(heroes_data, key=heroes_data.get)}')

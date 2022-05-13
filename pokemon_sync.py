import time
import requests

start_time = time.time()


for number in range(1, 15):
    print(number)
    url = f'https://pokeapi.co/api/v2/pokemon/{number}'
    resp = requests.get(url)
    pokemon = resp.json()
    print(pokemon['name'])

print("--- %s seconds ---" % (time.time() - start_time))
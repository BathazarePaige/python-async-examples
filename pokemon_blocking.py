import time 
import asyncio
import requests

start_time = time.time()

async def main():

    for number in range(1, 40):
        print(number)
        url = f'https://pokeapi.co/api/v2/pokemon/{number}'
        resp = requests.get(url)
        pokemon = resp.json()
        print(pokemon['name'])      

asyncio.run(main())
print("--- %s seconds ---" % (time.time() - start_time))
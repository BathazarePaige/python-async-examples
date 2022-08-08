import asyncio
import requests
import time

start_time = time.time()

async def main():
    loop = asyncio.get_event_loop()
    futures = [
        loop.run_in_executor(
            None, 
            requests.get, 
            f'https://pokeapi.co/api/v2/pokemon/{number}'
        )
        for number in range(1,40)
    ]
    for response in await asyncio.gather(*futures):
        print(response.status_code)
        
asyncio.run(main())
print("--- %s seconds ---" % (time.time() - start_time))
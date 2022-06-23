import asyncio
import concurrent.futures
import requests
import time

start_time = time.time()

async def main():

    with concurrent.futures.ThreadPoolExecutor() as executor:

        loop = asyncio.get_event_loop()
        for number in range(40):
            futures = [
                loop.run_in_executor(
                    executor, 
                    requests.get, 
                    f'https://pokeapi.co/api/v2/pokemon/{number}'
                )
                
            ]
        for response in await asyncio.gather(*futures):
            print(response.text)

asyncio.run(main())
print("--- %s seconds ---" % (time.time() - start_time))
import asyncio
import time
import requests
from amadeus import Client

amadeus = Client(log_level='debug')

start_time = time.time()

async def main():
 
        loop = asyncio.get_event_loop()
        futures = [
            loop.run_in_executor(
                None, 
                requests.get, 
                amadeus.reference_data.urls.checkin_links.get(
            airlineCode='BA')
            )
            for number in range(20)
            ]
        print("--- %s seconds ---" % (time.time() - start_time))
        for response in await asyncio.gather(*futures):
            print(response.status_code)


asyncio.run(main())
print("--- %s seconds ---" % (time.time() - start_time))
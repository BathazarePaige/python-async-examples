from amadeus import Client
import time 
import asyncio

amadeus = Client()

start_time = time.time()

async def main():

    for number in range(20):
        try:
            response = amadeus.reference_data.urls.checkin_links.get(
            airlineCode='BA')
            print(number)
            print(response.data)
                                    
        except:
            continue

asyncio.run(main())

print("--- %s seconds ---" % (time.time() - start_time))
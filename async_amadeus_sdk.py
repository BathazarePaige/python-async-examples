from amadeus import Client, ResponseError
import time 
import asyncio

amadeus = Client()

start_time = time.time()

async def main():

    try:
        for number in range(0, 10):
            response = amadeus.reference_data.urls.checkin_links.get(airlineCode='BA')
            print(response.data)       
                                        
    except ResponseError as error:
        raise error

asyncio.run(main())
print("--- %s seconds ---" % (time.time() - start_time))
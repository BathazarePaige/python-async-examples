from amadeus import Client, ResponseError
import time 

amadeus = Client()

start_time = time.time()
try:
    for number in range(0, 10):
        response = amadeus.reference_data.urls.checkin_links.get(airlineCode='BA')
        print(response.data)       
                                     
except ResponseError as error:
    raise error

end_time = time.time()
print(end_time - start_time)


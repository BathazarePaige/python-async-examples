import aiohttp
import asyncio
import time
import requests

AUTH_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"
headers = {"Content-Type": "application/x-www-form-urlencoded"}
data = {"grant_type": "client_credentials",
        "client_id": 'YOUR_CLIENT_ID',
        "client_secret": 'YOUR_CLIENT_SECRET'}

response = requests.post(AUTH_ENDPOINT,
                        headers=headers,
                        data=data)

access_token = response.json()['access_token']

start_time = time.time()

async def main():

    headers = {'Authorization': 'Bearer' + ' ' + access_token}
    
    flight_search_endpoint = 'https://test.api.amadeus.com/v2/reference-data/urls/checkin-links'
    parameters = {"airlineCode": 'BA'}

    async with aiohttp.ClientSession() as session:

        for number in range(0, 20):
            async with session.get(flight_search_endpoint,
                            params=parameters,
                            headers=headers) as resp:
                flights = await resp.json()
                print(flights)

asyncio.run(main())
print("--- %s seconds ---" % (time.time() - start_time))
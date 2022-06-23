# Asyncronous API calls in Python

In this repository we explore asynchronous API calls in Python.

To get started start your virtual environment and install the dependences:

```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

Also, if you want to test the Amadeus APIs, you will need to create an account and get your API key/secret from the [developer's portal](https://developers.amadeus.com/).

### Make Async API calls using aiohttp 

In the file `amadeus_aiohttp` you can call the the Amadeus Flight-Checkin link API using the `aiohttp` library. The code runs in an async way

### Wrap the Amadeus SDK in an async function

At this point we wanted to experiment if we could run in an asynchronous way a bunch of API calls. However it was proved it's not possible since Asyncio CANNOT run blocking code in an async way. You can run the code example at `amadeus_blocking`.

Since Amadeus offers a Python SDK which uses the blocking library `requests.py`, how can we use the library in an asynchronous application?

### Thread executor

The solution is to use a thread executor, in order to run the blocking call in separate threads without affecting the async loop, as it's implemented in the script `amadeus_threads.py`.









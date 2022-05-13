import asyncio
import time

start_time = time.time()

async def async_count():
    print('One')
    await asyncio.sleep(1)
    print('Two')

async def main():
    await asyncio.gather(async_count(), async_count(), async_count())

def sync_count():
    print('One')
    time.sleep(1)
    print('Two')

def sync_count_total():
    sync_count()
    sync_count()
    sync_count()

if __name__ == "__main__":
    # sync_count_total()
    asyncio.run(main())
    print("--- %s seconds ---" % (time.time() - start_time))
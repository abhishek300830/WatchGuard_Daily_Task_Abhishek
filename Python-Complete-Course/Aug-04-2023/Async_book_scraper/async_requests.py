import aiohttp
import asyncio
import time
import async_timeout


async def fetch_page(session, url):
    start_time = time.time()
    async with async_timeout.timeout(10):
        async with session.get(url) as response:
            print(f"response {response.status} Time Taken {time.time() - start_time}")
            return response.status


async def get_multiple_pages(loop, *urls):
    tasks = []
    async with aiohttp.ClientSession(loop=loop) as session:
        for url in urls:
            tasks.append(fetch_page(session, url))

        group_tasks = asyncio.gather(*tasks)
        return await group_tasks


loop = asyncio.get_event_loop()

urls = ['http://google.com' for i in range(50)]
# loop.run_until_complete(fetch_page('http://google.com'))

start_time_outer = time.time()
loop.run_until_complete(get_multiple_pages(loop, *urls))
print(f"Time Taken to complete {time.time() - start_time_outer}")

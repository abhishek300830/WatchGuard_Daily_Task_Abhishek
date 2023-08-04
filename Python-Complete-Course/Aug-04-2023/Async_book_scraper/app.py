import requests
import logging
import time
import async_timeout
import aiohttp
import asyncio


import pages
from pages.all_book_page import AllBooksPage

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s [%(filename)s : %(lineno)d] %(message)s',
    datefmt='%d-%m-%Y %H:%M:%S',
    level=logging.DEBUG,
    filename='logs.txt'
)

logger = logging.getLogger("scraping")

logger.info("Loading Books List ...")

page_content = requests.get("https://books.toscrape.com").content
page = AllBooksPage(page_content)

loop = asyncio.get_event_loop()

books = page.books


async def fetch_page(session, url):
    start_time = time.time()
    async with async_timeout.timeout(10):
        async with session.get(url) as response:
            print(f"response {response.status} Time Taken {time.time() - start_time}")
            return await response.text()


async def get_multiple_pages(loop, *urls):
    tasks = []
    async with aiohttp.ClientSession(loop=loop) as session:
        for url in urls:
            tasks.append(fetch_page(session, url))

        group_tasks = asyncio.gather(*tasks)
        return await group_tasks

urls = [f'https://books.toscrape.com/catalogue/page-{page_no + 1}.html' for page_no in range(1,50)]
start =time.time()
pages = loop.run_until_complete(get_multiple_pages(loop,*urls))
print(f"Total Pages request took {time.time()-start}")

for page_content in pages:
    logger.debug('creating all book page from content.')
    page = AllBooksPage(page_content)
    books.extend(page.books)

# for page_no in range(1, 50):
#     url = f"https://books.toscrape.com/catalogue/page-{page_no + 1}.html"
#     page_content = requests.get(url).content
#     logger.debug("Creating all book page from Page content.")
#     page = AllBooksPage(page_content)
#     books.extend(page.books)

# run menu file to run program

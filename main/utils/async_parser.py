import aiohttp
import asyncio
import time
import json
from bs4 import BeautifulSoup

search_link = 'https://www.cocobee.kz/search/index.php?q={code}&s=Найти'


def read_json(file):
    with open(file, mode='r', encoding='utf-8') as f:
        return json.load(f)





async def main():
    barcodes = read_json('products.json').get('barcodes')

    start_time = time.time()

    async with aiohttp.ClientSession() as session:
        tasks = []

        for code in barcodes:
            tasks.append(fetch_page(session, search_link.format(code=code)))

        htmls = await asyncio.gather(*tasks)

    end_time = time.time()

    total_found = 0
    total_not_found = 0

    found_codes = []


    for url, html in zip([search_link.format(code=code) for code in barcodes], htmls):
        wrap = html.find('div', {'class': 'search-advanced-result'})

        found = wrap.get_text(strip=True).split()[-1]

        code = ''.join(list(filter(lambda x: x.isdigit(), url)))

        if found == '0':
            total_not_found += 1

        elif found == '1':
            total_found += 1
            found_codes.append(code)

        print(f"Content from {url}:\n{found}\n")
        with open('not_found.json', 'w', encoding='utf-8') as f:
            json.dump(found_codes, f)

    print(f'total found: {total_found}\ntotal not found: {total_not_found}')
    print(f"Time taken: {end_time - start_time} seconds")


async def fetch_page(session, url):
    async with session.get(url) as response:
        content =  await response.text()

        # parse HTML content using BeautifulSoup
        soup = BeautifulSoup(content, 'html.parser')
        # return parsed HTML
        return soup


asyncio.run(main())
import json
from pprint import pprint

import requests
from bs4 import BeautifulSoup


def write_json(data: list, filename: str):
    with open(filename, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def read_json(filename: str):
    with open(filename, "r", encoding='utf-8') as f:
        data = json.load(f)
    return data


BASE_URL = 'https://www.cocobee.kz/'


def get_soup(url: str) -> BeautifulSoup:
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup


def get_catalog_items():
    soup = get_soup(f'{BASE_URL}/catalog/')
    result = []
    wrapper = soup.find('div', class_='i_sect_list')
    upper_items = wrapper.find_all('div', class_='i_sl_1')
    for idx, upper_item in enumerate(upper_items):
        name = upper_item.find('a', class_='i_sl_title').get_text(strip=True)
        link = upper_item.find('a', class_='i_sl_title').get('href')
        inner_items = upper_item.find('ul').find_all('li')

        print(f'[UPPER] - {name}')
        result.append({
            'name': name,
            'link': link,
            'inner_items': []
        })
        for inner_item in inner_items:
            inner_name = inner_item.get_text(strip=True)
            inner_link = inner_item.find('a').get('href')
            print(f'----[INNER] - {inner_name}')
            result[idx]['inner_items'].append({
                'name': inner_name,
                'link': inner_link,
            })
    return result


# json_data = get_catalog_items()
# write_json(json_data, 'data.json')


codes = [
    9785436607283,
    9785436603629,
    9785436603773,
    9785436603100,
    9785436609300
]

search_link = 'https://www.cocobee.kz/search/index.php?q={code}&s=Найти'


# for code in codes:
#     soup = get_soup(search_link.format(code=code))
#     item = soup.find('div', class_='i_item jq_item')
#     print(item)

def get_products_by_barcodes(codes_list: list):
    result = []
    for code in codes_list:
        soup = get_soup(search_link.format(code=code))
        item = soup.find('div', class_='i_item jq_item')

        name = item.find('a', class_='i_item_name').get_text(strip=True)
        link = item.find('a', class_='i_item_name').get('href')
        price = item.find('span', class_='i_price').get_text(strip=True)
        preview = item.find('img').get('src')

        # print(f'[{name}] - {link} - {price} - {preview}')

        inner_soup = get_soup(f'{BASE_URL}{link}')

        category_block = inner_soup.find('div', class_='i_ai_content j_ai_content').find_all('div', class_='idn')[1]
        i_item = category_block.find_all('div', class_='i_cele_property_col i_cele_prop_link')

        description = inner_soup.find('div', class_='i_ai_content j_ai_content').find_all('div', class_='idn')[0].get_text(strip=True)
        categories = [j.get_text(strip=True) for j in i_item[1].find_all('a')]
        publishing_house = i_item[2].get_text(strip=True)

        result.append({
            'name': name,
            'slug': link.split('/')[-2],
            'description': description,
            'price': price,
            'preview': preview,
            'categories': categories,
            'publishing_house': publishing_house,
        })
    return result

products_data = get_products_by_barcodes(codes)
write_json(products_data, 'products.json')


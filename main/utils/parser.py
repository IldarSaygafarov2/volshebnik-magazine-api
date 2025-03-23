import json

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


json_data = get_catalog_items()
write_json(json_data, 'data.json')

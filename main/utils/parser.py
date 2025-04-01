# import json
#
# import requests
# from bs4 import BeautifulSoup
#
#
# def write_json(data: list, filename: str):
#     with open(filename, "w", encoding='utf-8') as f:
#         json.dump(data, f, indent=4, ensure_ascii=False)
#
#
# def read_json(filename: str):
#     with open(filename, "r", encoding='utf-8') as f:
#         data = json.load(f)
#     return data
#
#
# BASE_URL = 'https://www.cocobee.kz/'
#
#
# def get_soup(url: str) -> BeautifulSoup:
#     response = requests.get(url)
#     response.raise_for_status()
#     soup = BeautifulSoup(response.text, 'html.parser')
#     return soup
#
#
# # codes = [
# #     9785436607283,
# #     9785436603629,
# #     9785436603773,
# #     9785436603100,
# #     9785436609300
# # ]
#
# search_link = 'https://www.cocobee.kz/search/index.php?q={code}&s=Найти'
#
#
# def get_categories_data():
#     soup = get_soup(BASE_URL + 'catalog/')
#
#     wrapper = soup.find('div', {'class': 'i_sect_list'})
#
#     items = wrapper.find_all('div', {'class': 'i_sl_1'})
#
#     categories = {}
#
#     for item in items:
#         title = item.find('div', {'class': 'i_ml135'}).find('a', {'class': 'i_sl_title'}).get_text(strip=True)
#         categories[title] = []
#         for i in item.find('ul').find_all('li'):
#             inner_title = i.get_text(strip=True)
#             inner_slug = i.find('a').get('href').split('/')[-2]
#
#             categories[title].append({'title': inner_title, 'slug': inner_slug})
#
#     return categories
#
#
# def get_products_by_barcodes():
#     data = read_json('products.json')
#     not_found_barcodes = []
#     found_barcodes = []
#     for code in data.get('barcodes'):
#         try:
#             code = int(code)
#         except ValueError:
#             continue
#
#         link = search_link.format(code=code)
#         soup = get_soup(link)
#
#         wrap = soup.find('div', {'class': 'search-advanced-result'})
#
#         found = wrap.get_text(strip=True).split()[-1]
#
#         if found == '0':
#             print(f'barcode {code} not found')
#             not_found_barcodes.append(code)
#             continue
#         found_barcodes.append(code)
#
#     print('=' * 20)
#     result = {
#         'total_not_found': len(not_found_barcodes),
#         'total_found': len(found_barcodes),
#         'not_found_barcodes': not_found_barcodes,
#         'found_barcodes': found_barcodes,
#     }
#     write_json(result, 'not_found_barcodes.json')
#
#
# import time
#
# start = time.time()
# get_products_by_barcodes()
#
# end = time.time()
#
# print(f'total time {end - start}')
# # data = get_categories_data()
# # write_json(data, 'categories.json')

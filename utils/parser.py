import json

import requests
from bs4 import BeautifulSoup

test_url = 'https://maguss.ru/catalog/12061/'


def get_preview_and_images(list_object: list):
    if not list_object:
        return ""
    return list_object.pop(0), list_object


def get_soup(url: str, headers=None) -> BeautifulSoup:
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup


def parse_robins_site_images(images_page_url: str):
    soup = get_soup(images_page_url)
    wrapper = soup.find("div", {"class": "flexslider-big"})
    images = [i.get("src") for i in wrapper.find_all("img")]
    return get_preview_and_images(images)


def parse_kristall_kanc_site_images(images_page_url: str):
    soup = get_soup(images_page_url)
    wrapper = soup.find('div', class_='detail-gallery-big-slider-main__ratio-inner')
    images = wrapper.find_all('img', class_='detail-gallery-big__picture')
    images = [i.get('src') for i in images]
    return get_preview_and_images(images)


def parse_moy_lvenok_site_images(images_page_url: str):
    soup = get_soup(images_page_url)
    wrapper = soup.find('ul', class_='thumbnails')
    images = [i.get('src') for i in wrapper.find_all('img')]
    return get_preview_and_images(images)


def parse_chitatel_site_images(images_page_url: str):
    soup = get_soup(images_page_url)
    wrapper = soup.find('div', class_='images-primary')
    images = [i.get('src') for i in wrapper.find_all('img')]
    return get_preview_and_images(images)


def parse_detmir_site_images(images_page_url: str):
    soup = get_soup(images_page_url)
    wrapper = soup.find('div', class_='bwg')
    images = [i.get("src") for i in wrapper.find_all('img')]
    return get_preview_and_images(images)


def parse_shkola7gnomov_site_images(images_page_url: str):
    soup = get_soup(images_page_url)
    wrapper = soup.find('div', id='product-gallery')
    images = [i.get("src") for i in wrapper.find_all('img')]
    return get_preview_and_images(images)


def parse_childrensmarket_site_images(images_page_url: str):
    # TODO: поменять 150х150 на 400х400
    soup = get_soup(images_page_url)
    wrapper = soup.find('div', class_='magnific-gallery')
    images = [i.get("src") for i in wrapper.find_all('img')]
    return get_preview_and_images(images)


def parse_maguss_site_images(images_page_url: str):
    soup = get_soup(images_page_url)
    wrapper = soup.find('div', class_='detail-gallery-big-slider')
    images = [i.get("src") for i in wrapper.find_all('img')]
    return get_preview_and_images(images)


# def parse_sima_land_site_images(images_page_url: str):
#     pass
#
#
# def parse_21vek_site_images(images_page_url: str):
#     pass
#
#
# def parse_bondibon_site_images(images_page_url: str):
#     pass
#
#
# def parse_chitai_gorod_site_images(images_page_url: str):
#     pass
#
#
# def parse_ozon_site_images(images_page_url: str):
#     pass
#
#
# def parse_wildberries_site_images(images_page_url: str):
#     pass
#
#
# def parse_litres_site_images(images_page_url: str):
#     pass
#
#
# def parse_labirint_site_images(images_page_url: str):
#     pass
#
#
# def parse_book24_site_images(images_page_url: str):
#     pass
#
#
# def parse_eksmo_site_images(images_page_url: str):
#     pass
#
#
# def parse_alpinabook_site_images(images_page_url: str):
#     pass
#
#
# def parse_bookvoed_site_images(images_page_url: str):
#     pass
#
#
# def parse_ast_ru_site_images(images_page_url: str):
#     pass

URLS = {
    "robins.ru": parse_robins_site_images,
    "kristall-kanc.ru": parse_kristall_kanc_site_images,
    "moy-lvenok.ru": parse_moy_lvenok_site_images,
    "chitatel.by": parse_chitatel_site_images,
    "www.detmir.ru": parse_detmir_site_images,
    "shkola7gnomov.ru": parse_shkola7gnomov_site_images,
    "childrensmarket.ru": parse_childrensmarket_site_images,
    "maguss.ru": parse_maguss_site_images,
}


def parse_images_by_domain(domain: str, page_url: str):
    return URLS.get(domain)(page_url)


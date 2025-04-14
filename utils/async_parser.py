import os
import json
from pathlib import Path
from pprint import pprint

import requests

from bs4 import BeautifulSoup

BASE_DIR = Path(__file__).resolve().parent.parent.parent


search_link = "https://www.cocobee.kz/search/index.php?q={code}&s=Найти"

BASE_URL = "https://www.cocobee.kz"


def read_json(file):
    with open(file, mode="r", encoding="utf-8") as f:
        return json.load(f)


def read_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
        return BeautifulSoup(content, "html.parser")


def save_html_page(content, filepath, filename):
    file_dir = BASE_DIR / filepath
    file_dir.mkdir(parents=True, exist_ok=True)

    with open(f"{file_dir}/{filename}", "w", encoding="utf-8") as f:
        f.write(content)


def get_soup(url):
    resp = requests.get(url).text
    soup = BeautifulSoup(resp, "html.parser")
    return soup


def parse_barcode_products():
    codes = read_json("found.json")
    for code in codes:
        soup = requests.get(search_link.format(code=code)).text
        save_html_page(soup, "barcode_files", f"code_{code}.html")


# parse_barcode_products()


def read_barcode_products_from_files():
    files = os.listdir("barcode_files")
    result = []
    for _file in files:
        barcode = "".join(list(filter(lambda x: x.isdigit(), _file)))
        print(f"processing {barcode}")
        if not barcode:
            print(f"no barcode ")
            continue
        with open(f"barcode_files/{_file}", "r", encoding="utf-8") as f:
            content = f.read()
            soup = BeautifulSoup(content, "html.parser")

        item = soup.find("div", {"class": "i_cs j_cs i_cs_tile"})
        if item is None:
            continue

        title = item.find("a", {"class": "i_item_name"}).get_text(strip=True)
        image = item.find("a", {"class": "i_item_img"}).find("img").get("src")
        price = item.find("span", {"class": "i_price"}).get_text(strip=True)
        url = item.find("a", {"class": "i_item_img"}).get("href")

        # detail_html = requests.get(f"{BASE_URL}{url}").text
        # save_html_page(
        #     detail_html, "barcode_files/details/", f"code_{barcode}_detail.html"
        # )

        result.append(
            {
                "barcode": barcode,
                "title": title,
                "image": image,
                "price": price,
                "url": url,
            }
        )
    return result


def read_barcode_product_detail():
    files = os.listdir("barcode_files/details/")
    result = []
    for idx, _file in enumerate(files, start=1):

        barcode = "".join(list(filter(lambda x: x.isdigit(), _file)))
        print(f"processing {idx}-{barcode}")
        with open(f"barcode_files/details/{_file}", "r", encoding="utf-8") as f:
            content = f.read()
            soup = BeautifulSoup(content, "html.parser")

            try:
                description = soup.find(
                    "div", {"class": "i_cele_dtxt jq_dtxt"}
                ).get_text()
            except AttributeError:
                print(barcode)
                description = ""

            swiper_container = soup.find("div", class_="swiper-container")
            photos_list = [i.get("src") for i in swiper_container.find_all("img")]

            result_item = {
                "description": description,
                "photos_list": photos_list,
            }

            wrapper = soup.find("div", {"class": "i_add_info_bl j_add_info_bl"})
            items = wrapper.find_all("div", {"class": "i_cele_property"})

            for item in items:
                cols = item.find_all("div", {"class": "i_cele_property_col"})
                left_item = cols[0].get_text(strip=True)
                right_item = cols[1].get_text(strip=True)

                result_item[left_item] = right_item
        result.append(result_item)

    return result


# data = read_barcode_products_from_files()

# inner_data = read_barcode_product_detail()

# final_result = []
# for idx, item in enumerate(data):
#     final_result.append(dict(**item, **inner_data[idx]))


# with open("final_result.json", "w", encoding="utf-8") as file:
#     json.dump(final_result, file, indent=4, ensure_ascii=False)


def download_photos_from_json():
    content = read_json("final_result.json")
    previews = [item.get("image") for item in content]
    galleries = [item.get("photos_list") for item in content]
    slugs = [item.get("url").split("/")[-2] for item in content]

    previews_dir = BASE_DIR / "media"
    previews_dir.mkdir(exist_ok=True)

    products_previews_dir = previews_dir / "products"
    products_previews_dir.mkdir(exist_ok=True)

    gallery_dir = products_previews_dir / "gallery"
    gallery_dir.mkdir(exist_ok=True)

    temp_result = {}
    for idx, preview in enumerate(previews):

        preview_url = BASE_URL + preview
        file_name = preview.split("/")[-1]
        data = requests.get(preview_url).content

        temp_result[slugs[idx]] = {"preview": file_name}
        with open(f"{products_previews_dir}/{file_name}", "wb") as _img:
            _img.write(data)
        print(f"downloaded: {file_name}")

    for idx, gallery in enumerate(galleries):
        _res = []

        for item in gallery:
            if item.startswith("https://"):
                url = item
            else:
                url = BASE_URL + item

            file_name = item.split("/")[-1]
            _res.append(file_name)

            data = requests.get(url).content
            with open(f"{gallery_dir}/{file_name}", "wb") as _img:
                _img.write(data)

            print(f"===== downloaded: {file_name}")

        temp_result[slugs[idx]]["gallery"] = _res
        print(f"gallery downloaded")

    with open("photos.json", mode="w", encoding="utf-8") as _file:
        json.dump(temp_result, _file, indent=4, ensure_ascii=False)


# download_photos_from_json()


def move_images_by_products_dir():
    content = read_json("final_result.json")
    previews = [item.get("image") for item in content]

    previews_in_media = os.listdir(BASE_DIR / "media/products")
    temp = []

    for i in previews_in_media:
        if i in previews:
            temp.append(i)

    print(temp)


# move_images_by_products_dir()

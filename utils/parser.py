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
    _images = []
    for image in images:
        image = image.replace('150x150', '450x450')
        _images.append(image)
    return get_preview_and_images(_images)


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
    call = URLS.get(domain)
    if call is None:
        return None, None
    return call(page_url)


temp = [
    "https://robins.ru/catalog/knigi-s-nakleykami/fotonakleyki-mir-zhivotnykh/",
    "https://robins.ru/catalog/knigi-s-nakleykami/fotonakleyki-v-zooparke/",
    "https://robins.ru/catalog/trafarety/moi-pervye-trafarety-dlya-malchikov/",
    "https://robins.ru/catalog/trafarety/moi-pervye-trafarety-dlya-devochek-new/",
    "https://robins.ru/catalog/knizhki-kartonki/knizhki-kartonki-zagadki-obmanki-frukty-i-yagody/",
    "https://robins.ru/catalog/knizhki-kartonki/knizhki-kartonki-zagadki-obmanki-dikie-zhivotnye-/",
    "https://robins.ru/catalog/uchebnye-posobiya-slovari/obuchayushchiy-igrovoy-trenazhyer-ya-chitayu-po-slogam-/",
    "https://robins.ru/catalog/uchebnye-posobiya-slovari/obuchayushchiy-igrovoy-trenazher-razvivaem-vnimanie-i-logiku/",
    "https://robins.ru/catalog/uchebnye-posobiya-slovari/obuchayushchiy-igrovoy-trenazher-izuchaem-slova-tsveta-i-formy/",
    "https://robins.ru/catalog/uchebnye-posobiya-slovari/obuchayushchiy-igrovoy-trenazhyer-azbuka-bukvar/",
    "https://robins.ru/catalog/knigi-s-nakleykami/vimmelbukh-s-nakleykami-nelepitsy/",
    "https://robins.ru/catalog/knigi-s-nakleykami/bolshaya-kniga-vimmelbukhov-2/?ysclid=m8u5uixur6785917079",
    "https://www.21vek.by/interactive_toys/4630017955817_bert_toys_8805675.html",
    "https://kristall-kanc.ru/catalog/khobbi_i_tvorchestvo/nabory_dlya_tvorchestva_1/76688/?ysclid=ma9llgdrwc729797858",
    "https://lunsvet.com/catalog/tovary_dlya_shkoly/dnevniki/dnevnik_shkolnyy_1_4kl_48l_a5_dovolnyy_poni_d48_0711/",
    "https://moy-lvenok.ru/lumicube-planshet-tk03-talky-pro-blue-33975",
    "https://www.bondibon.ru/product/mini_igry_razvivayushie_igrayu_gde_khochu_zhivotnye_lesa_s_taktilnymi_vstavkami_bondibon_vv6327/",
    "https://chitatel.by/catalog/book/1437808",
    "https://moy-lvenok.ru/lumicube-albom-dlya-fotografij-ponchiki-34744",
    "https://moy-lvenok.ru/lumicube-albom-dlya-fotografij-mini-ponchiki-33974",
    "https://www.detmir.ru/product/index/id/6178730/",
    "https://www.detmir.ru/product/index/id/6178706/?ysclid=ma9mljdheo340032579",
    "https://www.detmir.ru/product/index/id/6405444/?ysclid=ma9mn6f64f131960601",
    "https://www.detmir.ru/product/index/id/6662129/?ysclid=ma9mq5q5uk547300512",
    "https://www.detmir.ru/product/index/id/3618168/?ysclid=ma9mrslf9206491742",
    "https://shkola7gnomov.ru/catalog/interaktivnye-knizhki-knizhki-igrushki/chudo-pazly-kniga-s-1-pazlom-mashinki/",
    "https://www.detmir.ru/product/index/id/3618166/?ysclid=ma9mxnb4nz998141917",
    "https://www.detmir.ru/product/index/id/3618171/?ysclid=ma9myk5wqz608934385",
    "https://www.detmir.ru/product/index/id/6586394/?ysclid=ma9mz9cneh173241706&variant_id=6586394",
    "https://www.chitai-gorod.ru/product/pocemucka-masiny-3090604",
    "https://www.chitai-gorod.ru/product/pocemucka-kosmos-3090603",
    "https://www.chitai-gorod.ru/product/pocemucka-dinozavry-3090601",
    "https://www.chitai-gorod.ru/product/pocemucka-anatomia-3090599",
    "https://www.detmir.ru/product/index/id/6663485/?variant_id=6663485",
    "https://www.detmir.ru/product/index/id/6663486/?variant_id=6663486",
    "https://uz.ozon.com/product/logopedicheskie-tetradi-slogovaya-struktura-slova-rabochaya-tetrad-2068373073/?at=gpt4EMArxF5ZLA5GT5pmkV5hY9nlzJhZNnALwcj1X4G0",
    "https://uz.ozon.com/product/logopedicheskie-tetradi-razvitie-fonematicheskogo-sluha-rabo-2070412255/?at=LZtlB6RApUNz4XQESrrqvVjuZYG09vSkBqBDEsDZoMMn",
    "https://shkola7gnomov.ru/catalog/knigi-dlya-dou/logopedicheskie-tetradi-razvitie-svyaznoy-rechi/?ysclid=ma9nmocm47446593673",
    "https://uz.ozon.com/product/logopedicheskie-tetradi-izuchaem-osnovy-grammatiki-borshcheva-1978540452/?at=57twkBZoQcQ8qZ88hJ9P33QFvMONvgIzoW3mPTD9mw4N",
    "https://uz.ozon.com/product/detskaya-kniga-s-obemnymi-kartinkami-russkie-narodnye-skazki-1636927052/?at=BrtzWY719TpgXQ1NfPGlgJKTzO78kpc9qJRv3FODrW6",
    "https://www.detmir.ru/product/index/id/6263991/?ysclid=ma9o6mboo6427388168&variant_id=6263991",
    "https://www.detmir.ru/product/index/id/6360790/?variant_id=6360790",
    "https://www.detmir.ru/product/index/id/6610640/",
    "https://shkola7gnomov.ru/catalog/poznavatelnaya-literatura/slimentsiklopediya-dinozavry/?ysclid=ma9ofgdagm732750075",
    "https://www.detmir.ru/product/index/id/6653227/",
    "https://www.detmir.ru/product/index/id/6493554/?variant_id=6493554",
    "https://www.detmir.ru/product/index/id/6057079/?variant_id=6057079",
    "https://www.detmir.ru/product/index/id/4110515/?variant_id=4110515",
    "https://www.bondibon.ru/product/logicheskaya_igra_bondilogika_bondibon_alisa_v_skazochnom_korolevstve_art_8688_a01_vv5564/",
    "https://www.bondibon.ru/product/konstruktor_magnitnyy_bondilogika_bondibon_cirkachi_moy_pervyy_ekvilibr_vv5676/",
    "https://www.bondibon.ru/product/igra_viktorina_umnaya_sova_turnir_znaniy_200_voprosov_box_vv6349/",
    "https://www.bondibon.ru/catalog/?q=%D0%98%D0%93%D0%A0%D0%90%D0%AE%20%D0%93%D0%94%D0%95%20%D0%A5%D0%9E%D0%A7%D0%A3%20%22%D0%9A%D0%9E%D0%9B%D0%9E%D0%91%D0%9E%D0%9A",
    "https://www.bondibon.ru/product/mini_igry_razvivayushie_igrayu_gde_khochu_azbuka_s_obemnymi_bukvami_bondibon_vv6324/",
    "https://www.bondibon.ru/product/mini_igry_razvivayushie_igrayu_gde_khochu_izuchaem_emocii_s_zerkalom_bondibon_vv6321/",
    "https://www.bondibon.ru/product/igra_nastolnaya_bondibon_bondilogika_logikubiki_box_vv6163/",
    "https://www.bondibon.ru/product/moy_pervyy_putevoditel_strany_mira_igra_viktorina_serii_umnaya_sova_vv5977/",
    "https://www.bondibon.ru/product/mini_igry_razvivayushie_igrayu_gde_khochu_ozhivshie_dinozavry_s_podvizhnymi_elementami_bondibon_vv5965/",
    "https://www.bondibon.ru/product/mini_igry_razvivayushie_igrayu_gde_khochu_izuchaem_formy_i_cveta_s_derevyannymi_figurkami_bondibon_vv5962/",
    "https://www.bondibon.ru/product/igra_golovolomka_bondibon_bondilogika_montessorter_box_vv5947/",
    "https://www.bondibon.ru/product/mini_igry_v_dorogu_dlya_malyshey_malenkiy_detektiv_s_lupoy_iz_kartona_bondibon_vv5785/",
    "https://www.bondibon.ru/product/mini_igry_razvivayushie_igrayu_gde_khochu_podelki_applikacii_otkrytki_svoimi_rukami_s_ispolzovaniem_podruchnykh_materialov_bondibon_vv5778/",
    "https://www.bondibon.ru/product/mini_igry_v_dorogu_dlya_malyshey_izuchaem_alfavit_so_stirayushimsya_markerom_bondibon_vv5728/",
    "https://www.bondibon.ru/product/mini_igry_razvivayushie_igrayu_gde_khochu_izuchaem_schet_s_derevyannymi_schetami_bondibon_vv5726/",
    "https://shkola7gnomov.ru/catalog/detskie-nastolnye-igry/mini-igry-v-dorogu-dlya-malyshey-chto-skryvaet-temnota-s-fonarikom-iz-kartona-art-vv5623/",
    "https://shkola7gnomov.ru/catalog/interaktivnye-knizhki-knizhki-igrushki/mini-igry-razvivayushchie-igrayu-gde-khochu-protivopolozhnosti-s-taktilnymi-vstavkami-art-vv5475/",
    "https://shkola7gnomov.ru/catalog/interaktivnye-knizhki-knizhki-igrushki/mini-igry-razvivayushchie-igrayu-gde-khochu-vimmelbukh-naydi-pokazhi-soschitay-art-vv5474/",
    "https://shkola7gnomov.ru/catalog/interaktivnye-knizhki-knizhki-igrushki/mini-igry-razvivayushchie-igrayu-gde-khochu-poglad-menya-s-tekstilnymi-vstavkami-art-vv5473/",
    "https://childrensmarket.ru/products/mini-igry-razvivayuschie-igrayu-gde-hochu-izuchaem-vremya-s-tsiferblatom-bondibon-gtwst-vv5472",
    "https://childrensmarket.ru/products/nastolnaya-igra-logodomino-slovo-iz-slogov-2-v-1-igraj-dumaj-uchis-bondibon-gtwst-vv5390",
    "https://shkola7gnomov.ru/catalog/detskie-nastolnye-igry/igra-viktorina-umnaya-sova-veselyy-alfavit-art-vv5372/",
    "https://shkola7gnomov.ru/catalog/detskie-nastolnye-igry/razvivayushchaya-igra-dlya-doshkolnikov-bolty-i-gayki-art-vv5368/",
    "https://shkola7gnomov.ru/catalog/detskie-nastolnye-igry/mini-igry-v-dorogu-dlya-malyshey-malyshi-dumayut-2-mozaika-magnitnaya-art-vv5350/",
    "https://shkola7gnomov.ru/catalog/detskie-nastolnye-igry/mini-igry-v-dorogu-dlya-malyshey-vodnye-raskraski-5-mnogorazovye-s-kistyu-art-vv5346/",
    "https://shkola7gnomov.ru/catalog/knizhki-aktiviti/mini-igry-v-dorogu-dlya-malyshey-vodnye-raskraski-4-art-vv5327/",
    "https://shkola7gnomov.ru/catalog/knizhki-aktiviti/mini-igry-v-dorogu-dlya-malyshey-vodnye-raskraski-3-art-vv5326/",
    "https://shkola7gnomov.ru/catalog/detskie-nastolnye-igry/nastolnaya-igra-loto-zhivotnyy-mir-igray-dumay-uchis-bondibon-art-vv4870/",
    "https://childrensmarket.ru/products/nastolnaya-igra-na-lipuchkah-sorter-kto-chto-est-igraj-dumaj-tvori-bondibon-gtwst-vv4771?ysclid=magllbax4n732920567",
    "https://childrensmarket.ru/products/nastolnaya-igra-na-lipuchkah-sorter-chej-malysh-igraj-dumaj-tvori-bondibon-gtwst-vv4768",
    "https://childrensmarket.ru/products/nastolnaya-igra-loto-kto-eto-spryatalsya-3-v-1-igraj-dumaj-uchis-bondibon-gtwst-vv4706",
    "https://childrensmarket.ru/products/kompaktnye-razvivayuschie-igry-v-dorogu-vodnye-raskraski-mnogorazovye-gtwst-vv4223",
    "https://childrensmarket.ru/products/obuchayuschie-igry-bondibon-nastolnaya-igra-fruktomaniya-box-172x45x142-sm-gtwst-%D0%92%D0%923447",
    "https://www.detmir.ru/product/index/id/6302242/",
    "https://uz.ozon.com/product/entsiklopediya-dlya-devochek-bukva-lend-entsiklopediya-sovremennoy-devchonki-kniga-dlya-devochek-818730759/?__rr=1",
    "https://www.detmir.ru/product/index/id/6187341/?variant_id=6187341",
    "https://maguss.ru/catalog/12061/",
    "https://samara.markertoys.ru/catalog/detskie_knigi/entsiklopedii/kniga_978_5_378_35197_8_super_entsiklopediya_dlya_devochek_moda_i_stil/?ysclid=mb3kc9jf8m720010866",
    "https://chitatel.by/catalog/book/258503?ysclid=mai60vmk35638717296",
    "https://robins.ru/catalog/khudozhestvennaya-literatura/chitaem-doma-i-v-detskom-sadu/",
    "https://robins.ru/catalog/knizhki-kartonki/taktilnaya-knizhka-transport/",
    "https://robins.ru/catalog/knizhki-kartonki/taktilnaya-knizhka-domashnie-zhivotnye-/",
    "https://robins.ru/catalog/knizhki-kartonki/taktilnaya-knizhka-dlya-malysha/",
    "https://robins.ru/catalog/knizhki-kartonki/taktilnaya-knizhka-dikie-zhivotnye-/",
    "https://robins.ru/catalog/khudozhestvennaya-literatura/taymless-izumrudnaya-kniga/"
]

for i in temp:
    domain = i.split("/")[2]
    preview, images = parse_images_by_domain(domain, i)


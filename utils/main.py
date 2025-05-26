def get_site_name_from_url(url: str) -> str:
    url_list = url.split('/')
    return [i for i in url_list if i][1]

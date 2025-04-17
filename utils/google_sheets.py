from pprint import pprint
from typing import Dict, List
from gspread import Client, Spreadsheet, Worksheet, service_account

GOOGLE_SHEET_URL = "https://docs.google.com/spreadsheets/d/1ovrfMEvJWpkttXBq9cp_i2aLJcGWS2X8vQF_bfStuZA/edit?gid=1128242186#gid=1128242186"
TABLE_ID = "1ovrfMEvJWpkttXBq9cp_i2aLJcGWS2X8vQF_bfStuZA"


def client_init_json() -> Client:
    return service_account(filename="volshebnik-content-table-36ed1851bb8d.json")


def get_table_by_url(client: Client, table_url: str):
    return client.open_by_url(table_url)


def get_table_by_key(client: Client, table_key: str):
    return client.open_by_key(table_key)


def test_get_table(table_url: str, table_key: str):
    client = client_init_json()
    table = get_table_by_url(client, table_url)
    print(f"Инфо о таблице по ссылке: {table}")
    table = get_table_by_key(client, table_key)
    print(f"Инфо о таблице по id: {table}")


def extract_data_from_sheet_var_2(table: Spreadsheet, sheet_name: str) -> List[Dict]:
    """
    Извлекает данные из указанного листа таблицы Google Sheets и возвращает список словарей.

    :param table: Объект таблицы Google Sheets (Spreadsheet).
    :param sheet_name: Название листа в таблице.
    :return: Список словарей, представляющих данные из таблицы.
    """
    worksheet = table.worksheet(sheet_name)
    headers = worksheet.row_values(1)  # Первая строка считается заголовками

    data = []
    rows = worksheet.get_all_values()[1:]  # Начинаем считывать с второй строки

    for row in rows:
        row_dict = {headers[i]: value for i, value in enumerate(row)}
        data.append(row_dict)

    return data


def get_items():
    client = client_init_json()
    table = get_table_by_url(client, GOOGLE_SHEET_URL)
    data = extract_data_from_sheet_var_2(table=table, sheet_name="Лист1")
    return data

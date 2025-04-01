from openpyxl import load_workbook
import json

wb = load_workbook(filename='products.xlsx')
sheet = wb.active

count = 0
result = {
    'barcodes': [],
    'publishers': [],
    'names': []
}
for i in sheet:
    if i[1].value not in result['barcodes']:
        result['barcodes'].append(i[1].value)
    if i[2].value not in result['names']:
        result['names'].append(i[2].value)
    if i[3].value not in result['publishers']:
        result['publishers'].append(i[3].value)


with open('products.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=4)

# wb.save('products.xlsx')
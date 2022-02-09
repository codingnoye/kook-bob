import requests
from ast import literal_eval
import re

def get_menu(today):
    res = requests.get(f'https://kmucoop.kookmin.ac.kr/menu/menujson.php?sdate={today}&edate={today}&today={today}')
    text = res.text.replace('\\r\\n', '\\n').replace('<br>', ' - ').replace('\\\\', '\\n').replace('\\n\\n', '\\n').replace('<sup>', '').replace('<\\/sup>', '')
    data = literal_eval(text)
    price_pattern = re.compile('[0-9,]+')

    parsed = {}

    for cafeteria_name, day in data.items():
        if not day: continue
        cafeteria = {'name': cafeteria_name, 'corners': []}
        for corner_name, menu in day[today].items():
            corner = {'name': corner_name, 'blocks': []}
            name = menu['메뉴']
            price = menu['가격']
            if name=='': continue
            names = name.split('\n')
            prices = price.split('\n')
            
            items = names + prices
            blocks = [[]]
            for item in items:
                if item.strip() == '': continue
                blocks[-1].append(item)
                if price_pattern.match(item):
                    blocks.append([])
            if len(blocks[-1]) == 0: blocks.pop()

            corner['blocks'] = blocks
            cafeteria['corners'].append(corner)
        parsed[cafeteria_name] = cafeteria
    
    return parsed
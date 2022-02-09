import datetime as dt
import parser
import json

def get_today():
    return dt.date.today().strftime("%Y-%m-%d")

def json_prettify(data):
    return json.dumps(data, indent=2, ensure_ascii=False)

if __name__ == '__main__':
    today = get_today()
    parsed = parser.get_menu(today)
    print(json_prettify(parsed))
import requests

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

def get_url():
    url = 'https://min-api.cryptocompare.com/data/v2/histoday?fsym=BTC&tsym=USD&limit=1000'
    response = requests.get(url)
    jsonData = response.json()
    data = jsonData["Data"]["Data"]
    index = 0
    for item in data:
        time = item["time"]
        open = item["open"]
        close = item["close"]
        high = item["high"]
        low = item["low"]
        index = index + 1
        doc = {
            'time': time,
            'open': open,
            'close': close,
            'high': high,
            'low': low
        }
        db.btcdb.insert_one(doc)
        print(str(index) + "번째 데이터 수집 완료")

db.btcdb.drop()
get_url()
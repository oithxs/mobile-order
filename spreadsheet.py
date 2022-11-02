import requests
import json
import datetime
from pytz import timezone
import random
import os
from dotenv import load_dotenv

# .envファイルの内容を読み込見込む
load_dotenv()

def main(order_item):
    ORDER_ID = random.randint(100,999)

    url = os.environ['GAS_URL']
    headers = {
        'Content-Type': 'application/json',
    }
    data = {
        "id": ORDER_ID,
        "cheese": order_item[0],
        "butter": order_item[1],
        "salt": order_item[2],
        "curry": order_item[3],
        "time": get_time()
    }

    response = requests.post(url, data=json.dumps(data), headers=headers)
    if(response.status_code == 200):
        return ORDER_ID
    return 0

def get_time():
  now = datetime.datetime.now(timezone('Asia/Tokyo'))
  return now.time().strftime('%X')
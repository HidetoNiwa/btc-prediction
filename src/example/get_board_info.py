# https://snuow.com/2021/11/%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%A0/coincheck-api/

import requests
import pandas as pd
# apiを叩くためのURL
url = 'https://coincheck.com/api/trades?pair=btc_jpy&limit=200'
# 取得データをjsonで格納します
coincheck = requests.get(url).json()
# pandasでデータフレームにして表示
pd.DataFrame(coincheck['data'])

print(pd.DataFrame(coincheck['data']))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 参考サイト
# https://di-acc2.com/programming/python/15316/

import json
import requests
import pandas as pd

import threading
import time

import datetime

btc_rate = pd.DataFrame(columns=['id', 'amount', 'rate'])


class name:
    json = '../setting.json'

    def json_import():
        f = open(name.json, 'r')
        json_dict = json.load(f)
        return json_dict


def get_board_info():
    BASE_URL = 'https://coincheck.com'
    url = BASE_URL + '/api/trades'

    params = {
        'pair': 'btc_jpy'
    }

    data = requests.get(url, params=params)
    data = data.json()
    if data['success'] == True:
        print(pd.DataFrame(data['data']))


def scheduler(interval, f, wait=True):
    base_time = time.time()
    next_time = 0
    while True:
        t = threading.Thread(target=f)
        t.start()
        if wait:
            t.join()
        next_time = ((base_time - time.time()) % interval) or interval
        time.sleep(next_time)


if __name__ == '__main__':
    print("Starting...")
    # api = name.json_import()
    # print(api)
    today = datetime.datetime.now()
    output_file_name = str(today.year)+str(today.month) + \
        str(today.day)+str(today.hour)
    print(output_file_name)

    scheduler(10, get_board_info, False)

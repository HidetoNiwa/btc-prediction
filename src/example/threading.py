# https://qiita.com/montblanc18/items/05715730d99d450fd0d3

import time
import threading


def worker():
    print(time.time())
    time.sleep(8)


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


scheduler(0.1, worker, False)

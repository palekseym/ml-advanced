import cryptocompare
import json
import socket
import socks
import time
from tqdm.auto import tqdm
from joblib import delayed, Parallel
from itertools import cycle


def get_history(ticker, port):

    socks.set_default_proxy(socks.PROXY_TYPE_SOCKS5, '127.0.0.1', port)
    socket.socket = socks.socksocket

    day_30 = cryptocompare.get_historical_price_day(ticker, curr='USD', limit=30)
    day_3 = cryptocompare.get_historical_price_hour(ticker, curr='USD', limit=3*24)
    hour_1 = cryptocompare.get_historical_price_minute(ticker, curr='USD', limit=60)

    for o, file_name in [(day_30, f"data/{ticker}_30.json"), (day_3, f"data/{ticker}_3.json"), (hour_1, f"data/{ticker}_1.json")]:
        if o is not None:
            with open(file_name, 'w') as f:
                json.dump(o, f)
    time.sleep(1.5)


# Количесво потоков сбора
__COUNT__REQUEST__ = 2


if __name__ == '__main__':
    ports = cycle([9050, 9060, 9070, 9080])

    with open('tickers_500.json', 'r') as f:
        coin_list = json.load(f)

    # files = [f.name.split('_')[0] for f in Path('data').glob('*_3.json')]
    # coin_list = list(set(coin_list) - set(files))

    with Parallel(n_jobs=__COUNT__REQUEST__) as parallel, tqdm(total=len(coin_list)) as bar:
        while len(coin_list) > 0:
            q = []
            for i in range(50):
                try:
                    q.append([coin_list.pop(), next(ports)])
                except IndexError:
                    break

            parallel(delayed(get_history)(i[0], i[1]) for i in q)
            time.sleep(15)
            bar.update(len(q))




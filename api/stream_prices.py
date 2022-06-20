import json
import requests

import constants.defs as defs

STREAM_URL = f"https://stream-fxpractice.oanda.com/v3"

def stream_prices(pairs_list):
        params = dict(
            instruments=','.join(pairs_list)
        )

        url = f"{STREAM_URL}/accounts/{defs.ACCOUNT_ID}/pricing/stream"

        resp = requests.get(url, params=params, headers=defs.SECURE_HEADER, stream=True)

        for price in resp.iter_lines():
            if price:
                decoded_price = json.load(price.decode('utf-8'))
                print(decoded_price)
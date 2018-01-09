# -*- coding: utf-8 -*-

import hashlib
import requests
import urllib
import urllib.parse
import json
import hmac
import time

class Coinfalcon():

    def __init__(self, key, secret):
        self.key = key
        self.secret = secret
        self.endpoint = 'https://coinfalcon.com/api/v1'

    def get_headers(self, method, request_path, body={}):
        timestamp = str(int(time.time()))

        if method == 'GET':
            payload = '|'.join([timestamp, method, request_path])
        else:
            payload = '|'.join([timestamp, method, request_path, json.dumps(body, separators=(',', ':'))])

        message = bytes(payload, 'utf-8')
        secret = bytes(self.secret, 'utf-8')

        signature = hmac.new(secret, message, hashlib.sha256).hexdigest()
        return {
            "CF-API-KEY": self.key,
            "CF-API-TIMESTAMP": timestamp,
            "CF-API-SIGNATURE": signature
        }

    def create_order(self, body):
        url = self.endpoint + "/user/orders"
        headers = self.get_headers('POST', urllib.parse.urlparse(url).path, body)
        return requests.post(url, headers=headers, data=body).json()

    def my_orders(self):
        url = self.endpoint + "/user/orders"
        headers = self.get_headers('GET', urllib.parse.urlparse(url).path)
        return requests.get(url, headers=headers).json()

    def orderbook(self, market):
        url = self.endpoint + "/markets/{}/orders".format(market)
        return requests.get(url).json()

#need use your own key && secret
client = Coinfalcon(KEY, SECRET)
print(client.orderbook('IOT-BTC'))
print(client.my_orders())
print(client.create_order({'market': 'IOT-BTC', 'operation_type': 'market_order', 'order_type': 'buy', 'size': '100000000000000'}))

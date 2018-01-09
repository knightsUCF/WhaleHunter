#!/usr/bin/python3

# only returning 1 pair


import api
api = api.API()


def get_tape():
    print('Getting Luno tape')
    print(api.get('https://api.mybitx.com/api/1/tickers'))
    # print(api.get('https://api.mybitx.com/api/1/ticker'))



get_tape()

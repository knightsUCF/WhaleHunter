#!/usr/bin/python3


import api
api = api.API()


def get_tape():
    response = api.get('https://bitgrail.com/api/v1/markets')
    return response['response']['BTC']

'''
dump = get_tape()
print(api.readable(dump))

for i in dump:
    print (i['market'])
    print (i['bid'])
    print (i['volume'])
'''

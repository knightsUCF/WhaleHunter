#!/usr/bin/python3

#!/usr/bin/python3

import api
api = api.API()


def get_tape():
    response = api.get('https://api.kucoin.com/v1/market/open/symbols')
    return response['data']

'''
dump = get_tape()
print(api.readable(dump))


# symbol, buy, vol

for i in dump:
    print (i['symbol'])
    print (i['buy'])
    print (i['vol'])
'''

# https://www.reddit.com/r/RaiBlocks/comments/7my9yb/bitgrail_api/

def private_order(order, key, secret, payload):
    url = "https://bitgrail.com/api/v1/{0}".format(order)
    tosign = "&".join([i + '=' + str(payload[i]) for i in payload])
    sign = hmac.new(secret, tosign, hashlib.sha512)
    headers = {'KEY': key,
           'SIGNATURE': sign.hexdigest()}
    response = post(url, headers=headers, data=payload)
    return response.json()
    
    
    

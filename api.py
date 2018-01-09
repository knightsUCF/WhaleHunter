import requests
import pprint



class API():


    def get(self, url):
        response = requests.get(url)
        json_response = response.json()
        return json_response



    def post(self, url, data): # payload_data: data = "{\"userName\": \"joe\", \"password\": \"x\"}"
        response = requests.request('POST', url, data = data)
        return response # response.text, response.headers



    def post_with_header(self, url, data, header): # header format: {'element': data}
        response = requests.request('POST', url, data = data, header = header)
        return response



    def get_element_from_json_object(self, object, key):
        return object.json()[key]



    def readable(self, response): # pass get()
        pprint.pprint(response)



    def get_elements(self, response, key):
        elements = response[key]
        print(elements)



'''
elements = get_vlans_json['vlan_element']
for x in elements:
   print("VLAN: {0} \t NAME: {1}".format(x['vlan_id'], x['name']))
'''

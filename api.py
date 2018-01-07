
import requests
import pprint



class API():


	def get(self, url):
		response = requests.get(url)
		json_response = response.json()
		return json_response


	def readable(self, response): # pass get()
		pprint.pprint(response)


	def get_elements(self, response, key):
		elements = response[key]
		print (elements)



''' Example:

api = API()
response = api.get('https://www.bit-z.com/api_v1/tickerall')
pretty = api.readable(response)
print(pretty)

'''






'''


elements = get_vlans_json['vlan_element']

print("2930 VLANS:")

for x in elements:
   print("VLAN: {0} \t NAME: {1}".format(x['vlan_id'], x['name']))

'''

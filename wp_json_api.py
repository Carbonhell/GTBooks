import requests
from enum import Enum

class RequestType(Enum):
	HEROES = 'https://guardiantales.wiki/wp-json/wp/v2/heroes'
	ITEMS = 'https://guardiantales.wiki/wp-json/wp/v2/items'

def request_item(type, filter=None, fields=None):
	''' type: RequestType; filter: (key:value); fields: (values)''' 
	query = {}
	if filter:
		for key, value in filter.items():
			query['meta_key'] = key
			query['meta_value'] = value
	if fields:
		query['_fields'] = ','.join(fields)
	http_response = requests.get(type.value,params=query)
	http_response = http_response.json()
	return http_response

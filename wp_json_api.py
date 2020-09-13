import requests
from enum import Enum
from collections import defaultdict
from hero import Hero
from config import PER_PAGE


class RequestType(Enum):
	HEROES = 'https://guardiantales.wiki/wp-json/wp/v2/heroes'
	ITEMS = 'https://guardiantales.wiki/wp-json/wp/v2/items'

# TODO: declare the queue used for heroes and items based on whether the user wants to use redis or not
# TODO: enrich with more methods to run more particular queries over the cache
class APICache:
	__Heroes = defaultdict(Hero)

	@classmethod
	def get_hero(cls, name: str):
		return cls.__Heroes.get(name)

	@classmethod
	def get_or_create_hero(cls, name: str):
		return cls.__Heroes[name]

# Unusued right now. Might be used later on to fetch particular information from the API.
def request_item(type: RequestType, filter: dict =None, fields: list = None):
	''' Helper method to fetch a single hero based on some criteria. Type: RequestType; filter: (key:value); fields: (values)''' 
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

# TODO: let users choose between the cache type: redis or global dict
# TODO: generalize over both heroes and items
# TODO: lock the APICache while updating?
def load_heroes(api = RequestType.HEROES.value):
	''' Method called every day to load the information related to Heroes from the GuardianTales wiki to a local cache.'''
	http_response = requests.get(api, {'per_page':PER_PAGE}).json() # A list of dicts, each dict representing data about a particular Hero.
	for hero_data in http_response:
		hero: Hero = APICache.get_or_create_hero(hero_data['acf']['name'])
		if hero.version < hero_data['_links']['version-history'][0]['count']: # If version-history cannot be trusted, we can just switch to 'modified'
			hero.reload(hero_data)
		



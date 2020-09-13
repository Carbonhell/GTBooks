from wp_json_api import request_item, RequestType
from config import icons
from common import MalusType

class Hero:
	ATK_KEY = 'atk'
	HP_KEY = 'hp'
	DEF_KEY = 'def'
	HEAL_KEY = 'heal'
	CRIT_KEY = 'crit'
	DMGRED_KEY = 'damage_reduction'
	BASICRES_KEY = 'basic_resistance'
	LIGHTRES_KEY = 'light_resistance'
	DARKRES_KEY = 'dark_resistance'
	FIRERES_KEY = 'fire_resistance'
	EARTHRES_KEY = 'earth_resistance'
	WATERRES_KEY = 'water_resistance'
	HEIGHT_KEY = 'height'
	WEIGHT_KEY = 'weight'
	AGE_KEY = 'age'
	SPECIES_KEY = 'species'
	RARITY_KEY = 'rarity'
	ROLE_KEY = 'role'
	EL_KEY = 'element'
	STORY_KEY = 'story'
	PICTURE_KEY = 'picture'
	EVOLUTION1_KEY = 'evolution_1'
	EVOLUTION2_KEY = 'evolution_2'
	EVOLUTION3_KEY = 'evolution_3'
	EVOLUTION4_KEY = 'evolution_4'
	EVOLUTION5_KEY = 'evolution_5'
	EQUIPMENT_KEY = 'compatible_equipment'
	RATING_KEY = 'rating'
	NORMALATKNAME_KEY = 'normal_atk_name'
	NORMALATKDESC_KEY = 'normal_atk_description'
	CHAINSKILLNAME_KEY = 'chain_skill_name'
	CHAINSTATETRIGGER_KEY = 'chain_state_trigger'
	CHAINSTATERESULT_KEY = 'chain_state_result'
	CHAINSKILLDESC_KEY = 'chain_skill_description'
	SPECIALABILITYNAME_KEY = 'special_ability_name'
	SPECIALABILITYDESC_KEY = 'special_ability_description'
	PASSIVES_KEY = 'passives'
	COLORATING_KEY = 'colo_rating'
	ARENARATING_KEY = 'arena_rating'
	PVERATING_KEY = 'pve_rating'
	TAGS_KEY = 'tags'
	EXWEAPONS_KEY = 'exclusive_weapon'

	EL_COLORS = {
		'Basic': 0x707070,
		'Light': 0xf5b800,
		'Dark': 0x220036,
		'Fire': 0xcb3636,
		'Water': 0x2d84bc,
		'Earth': 0x8f4f1a
	}
	def __init__(self, name):
		self.name = name
		self.status = False
	def load(self):
		response = request_item(RequestType.HEROES, {'name':self.name})
		if response:
			response = response[0]
		else:
			return False
		self.status = True # TODO: true only if request 200ed
		self.link = response['link']
		self.full_name = response['title']['rendered']
		response = response['acf'] # important custom info
		self.atk = response[Hero.ATK_KEY]
		self.hp = response[Hero.HP_KEY]
		self.defense = response[Hero.DEF_KEY]
		self.heal = response[Hero.HEAL_KEY]
		self.crit = response[Hero.CRIT_KEY]
		self.dmgred = response[Hero.DMGRED_KEY]

		self.resistances = {}
		if response[Hero.BASICRES_KEY]: self.resistances['Basic'] = {'icon':icons['basic'], 'value': response[Hero.BASICRES_KEY]}
		if response[Hero.LIGHTRES_KEY]: self.resistances['Light'] = {'icon':icons['light'], 'value': response[Hero.LIGHTRES_KEY]}
		if response[Hero.DARKRES_KEY]: self.resistances['Dark'] = {'icon': icons['dark'], 'value': response[Hero.DARKRES_KEY]}
		if response[Hero.FIRERES_KEY]: self.resistances['Fire'] = {'icon': icons['fire'], 'value': response[Hero.FIRERES_KEY]}
		if response[Hero.EARTHRES_KEY]: self.resistances['Earth'] = {'icon': icons['earth'], 'value': response[Hero.EARTHRES_KEY]}
		if response[Hero.WATERRES_KEY]: self.resistances['Water'] = {'icon':icons['water'], 'value': response[Hero.WATERRES_KEY]}

		self.height = response[Hero.HEIGHT_KEY]
		self.weight = response[Hero.WEIGHT_KEY]
		self.age = response[Hero.AGE_KEY]
		self.species = response[Hero.SPECIES_KEY]
		self.rarity = response[Hero.RARITY_KEY]
		self.role = response[Hero.ROLE_KEY]
		self.element = response[Hero.EL_KEY]
		self.story = response[Hero.STORY_KEY]
		self.picture = response[Hero.PICTURE_KEY]
		self.evolutions_pictures = [ # Can have missing values, interpreted as False
			response[Hero.EVOLUTION1_KEY],
			response[Hero.EVOLUTION2_KEY],
			response[Hero.EVOLUTION3_KEY],
			response[Hero.EVOLUTION4_KEY],
			response[Hero.EVOLUTION5_KEY],
		]
		self.compatible_equipment = response[Hero.EQUIPMENT_KEY] # List of strings
		self.overall_rating = response[Hero.RATING_KEY]
		self.normal_atk_name = response[Hero.NORMALATKNAME_KEY]
		self.normal_atk_description = response[Hero.NORMALATKDESC_KEY]
		self.chain_skill_name = response[Hero.CHAINSKILLNAME_KEY]
		self.chain_state_trigger = MalusType.from_str(response[Hero.CHAINSTATETRIGGER_KEY])
		self.chain_state_result = MalusType.from_str(response[Hero.CHAINSTATERESULT_KEY])
		self.chain_skill_description = response[Hero.CHAINSKILLDESC_KEY]
		self.special_ability_name = response[Hero.SPECIALABILITYNAME_KEY]
		self.special_ability_description = response[Hero.SPECIALABILITYDESC_KEY]
		self.passives = response[Hero.PASSIVES_KEY]
		self.colo_rating = response[Hero.COLORATING_KEY]
		self.arena_rating = response[Hero.ARENARATING_KEY]
		self.pve_rating = response[Hero.PVERATING_KEY]
		self.tags = response[Hero.TAGS_KEY] # List of strings
		self.exclusive_weapons = response[Hero.EXWEAPONS_KEY] # List of dicts
														# TODO: cross reference items (with id? name too)
		
		

		self.scaled_picture = self.picture.split('.')
		self.scaled_picture[-2] += '-150x150' # Get the part of the url before the extension, and add the scale modifier
		self.scaled_picture = '.'.join(self.scaled_picture) # Recreate the url

		return True # Load successful
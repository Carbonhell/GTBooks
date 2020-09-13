from config import ICONS
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
	def __init__(self):
		self.version = 0 # Forces a reload from the API

	def reload(self, hero_data: dict):
		self.version = hero_data['_links']['version-history'][0]['count']
		self.link = hero_data['link']
		self.full_name = hero_data['title']['rendered']
		hero_data = hero_data['acf'] # important custom info
		self.atk = hero_data.get(Hero.ATK_KEY, '')
		self.hp = hero_data.get(Hero.HP_KEY, '')
		self.defense = hero_data.get(Hero.DEF_KEY, '')
		self.heal = hero_data.get(Hero.HEAL_KEY, '')
		self.crit = hero_data.get(Hero.CRIT_KEY, '')
		self.dmgred = hero_data.get(Hero.DMGRED_KEY, '')

		self.resistances = {}
		if hero_data.get(Hero.BASICRES_KEY): self.resistances['Basic'] = {'icon':ICONS['basic'], 'value': hero_data.get(Hero.BASICRES_KEY, '')}
		if hero_data.get(Hero.LIGHTRES_KEY): self.resistances['Light'] = {'icon':ICONS['light'], 'value': hero_data.get(Hero.LIGHTRES_KEY, '')}
		if hero_data.get(Hero.DARKRES_KEY): self.resistances['Dark'] = {'icon': ICONS['dark'], 'value': hero_data.get(Hero.DARKRES_KEY, '')}
		if hero_data.get(Hero.FIRERES_KEY): self.resistances['Fire'] = {'icon': ICONS['fire'], 'value': hero_data.get(Hero.FIRERES_KEY, '')}
		if hero_data.get(Hero.EARTHRES_KEY): self.resistances['Earth'] = {'icon': ICONS['earth'], 'value': hero_data.get(Hero.EARTHRES_KEY, '')}
		if hero_data.get(Hero.WATERRES_KEY): self.resistances['Water'] = {'icon':ICONS['water'], 'value': hero_data.get(Hero.WATERRES_KEY, '')}

		self.height = hero_data.get(Hero.HEIGHT_KEY, '')
		self.weight = hero_data.get(Hero.WEIGHT_KEY, '')
		self.age = hero_data.get(Hero.AGE_KEY, '')
		self.species = hero_data.get(Hero.SPECIES_KEY, '')
		self.rarity = hero_data.get(Hero.RARITY_KEY, '')
		self.role = hero_data.get(Hero.ROLE_KEY, '')
		self.element = hero_data.get(Hero.EL_KEY, '')
		self.story = hero_data.get(Hero.STORY_KEY, '')
		self.picture = hero_data.get(Hero.PICTURE_KEY, '')
		self.evolutions_pictures = [ # Can have missing values, interpreted as False
			hero_data.get(Hero.EVOLUTION1_KEY, ''),
			hero_data.get(Hero.EVOLUTION2_KEY, ''),
			hero_data.get(Hero.EVOLUTION3_KEY, ''),
			hero_data.get(Hero.EVOLUTION4_KEY, ''),
			hero_data.get(Hero.EVOLUTION5_KEY, ''),
		]
		self.compatible_equipment = hero_data.get(Hero.EQUIPMENT_KEY, '') # List of strings
		self.overall_rating = hero_data.get(Hero.RATING_KEY, '')
		self.normal_atk_name = hero_data.get(Hero.NORMALATKNAME_KEY, '')
		self.normal_atk_description = hero_data.get(Hero.NORMALATKDESC_KEY, '')
		self.chain_skill_name = hero_data.get(Hero.CHAINSKILLNAME_KEY, '')
		self.chain_state_trigger = hero_data.get(Hero.CHAINSTATETRIGGER_KEY, '')
		if self.chain_state_trigger:
			self.chain_state_trigger = MalusType.from_str(self.chain_state_trigger)
		self.chain_state_result = hero_data.get(Hero.CHAINSTATERESULT_KEY, '')
		if self.chain_state_result:
			self.chain_state_result = MalusType.from_str(self.chain_state_result)
		self.chain_skill_description = hero_data.get(Hero.CHAINSKILLDESC_KEY, '')
		self.special_ability_name = hero_data.get(Hero.SPECIALABILITYNAME_KEY, '')
		self.special_ability_description = hero_data.get(Hero.SPECIALABILITYDESC_KEY, '')
		self.passives = hero_data.get(Hero.PASSIVES_KEY, '')
		self.colo_rating = hero_data.get(Hero.COLORATING_KEY, '')
		self.arena_rating = hero_data.get(Hero.ARENARATING_KEY, '')
		self.pve_rating = hero_data.get(Hero.PVERATING_KEY, '')
		self.tags = hero_data.get(Hero.TAGS_KEY, '') # List of strings
		self.exclusive_weapons = hero_data.get(Hero.EXWEAPONS_KEY, '') # List of dicts, can be non present
														# TODO: cross reference items (with id? name too)

		self.scaled_picture = self.picture.split('.')
		self.scaled_picture[-2] += '-150x150' # Get the part of the url before the extension, and add the scale modifier
		self.scaled_picture = '.'.join(self.scaled_picture) # Recreate the url

		return True # Load successful
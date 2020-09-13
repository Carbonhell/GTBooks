from enum import Enum
from config import ICONS

class MalusType(Enum):
	INJURED = {'name': 'Injured', 'icon': ICONS['injured']}
	DOWNED = {'name': 'Downed', 'icon': ICONS['downed']}
	AIRBORNE = {'name': 'Airborne', 'icon': ICONS['airborne']}
	ALL = {'name': 'All', 'icon': ICONS['all_maluses']}
	NONE = None

	@classmethod
	def from_str(cls, word):
		if word == 'Injured':
			return cls.INJURED
		elif word == 'Downed':
			return cls.DOWNED
		elif word == 'Airborne':
			return cls.AIRBORNE
		elif word == 'All':
			return cls.ALL
		elif word == 'None':
			return cls.NONE
		else:
			raise NotImplementedError()
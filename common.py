from enum import Enum
from config import icons

class MalusType(Enum):
	INJURED = {'name': 'Injured', 'icon': icons['injured']}
	DOWNED = {'name': 'Downed', 'icon': icons['downed']}
	AIRBORNE = {'name': 'Airborne', 'icon': icons['airborne']}
	ALL = {'name': 'All', 'icon': icons['all_maluses']}

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
		else:
			raise NotImplementedError()
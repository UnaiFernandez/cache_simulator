import cache
import constants
import set

class Time:
	def __init__(self, rewr, hitmiss):
		self.rewr = rewr
		self.hitmiss = hitmiss

	def Tbt(self):
		return constants.Tmm + (cache.Cache.number_words_block()-1)*constants.Tbuff

	def accesstime(self): 
		if(self.hitmiss == "Cache hit"):
			return constants.Tcm
		else:
			if(set.Set.dirty()):
				return constants.Tcm + self.Tbt() + self.Tbt()
			else:
				return constants.Tcm + self.Tbt()


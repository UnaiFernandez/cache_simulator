import constants

class Time:
	def __init__(self, rewr, hitmiss, dirty, number_words_block):
		self.rewr = rewr
		self.hitmiss = hitmiss
		self.dirty = dirty
		self.number_words_block = number_words_block

	def Tbt(self):
		return constants.Tmm + (self.number_words_block-1)*constants.Tbuff

	def accesstime(self): 
		if(self.hitmiss == True):
			return constants.Tcm
		else:
			if(self.dirty == True):
				return constants.Tcm + self.Tbt() + self.Tbt()
			else:
				return constants.Tcm + self.Tbt()
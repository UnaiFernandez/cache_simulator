import constants

class Time:
	def __init__(self, rewr, hitmiss, dirty, number_words_block,table):
		self.rewr = rewr
		self.hitmiss = hitmiss
		self.dirty = dirty
		self.number_words_block = number_words_block
		self.table = table

	#this function calculates the access time of the cache memory
	def accesstime(self): 
		if(self.hitmiss == True):
			return constants.Tcm
		else:
			for i in range(len(self.table)):
				if(self.table[i][1] == 1):
					return constants.Tcm + constants.Tbt + constants.Tbt
				else:
					return constants.Tcm + constants.Tbt	
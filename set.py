import cache
class Set:
	def __init__(self, cache, table):
			self.cache = cache
			self.table = table


	def number_sets(self):
		cache.number_sets()

	def dirty(self):
		if(cache.Cache.rewr() == 1):
			return True
		else:
			return False

	







class Cache:
	def __init__(self, sword, sblock, sset, rpol, ad, rewr, table,access):
		self.sword = sword
		self.sblock = sblock
		self.sset = sset
		self.rpol =rpol
		self.ad = ad
		self.rewr = rewr
		self.table = table
		self.access = access

	def word(self):
		return self.ad//self.sword

	def number_blocks(self):
		return self.sblock//self.sword

	def number_words_block(self):
		return self.sblock//self.sword

	def number_words(self):
		return self.number_blocks()*self.number_words_block

	def block(self):
		return self.word()//self.number_blocks()

	def number_sets(self):
		return 8//self.sset

	def set(self):
		if(self.sset == 8):
			return 0
		else:
			return self.block()%self.number_sets()

	def tag(self):
		if(self.sset == 8):
			return self.block()
		else:
			return self.block()//self.number_sets()

	def hit_miss(self):
		for i in range(len(self.table)):
			for j in range(len(self.table[i])):
				if(self.table[i][j] == self.tag()):
					return "Cache hit"
				else:
					return "Cache miss"

	def hits(self):
		h = 0
		if(self.hit_miss() == True):
			h = h + 1
		return h
			
	def hit_rate(self):
		return self.hits()/self.access

	def dirty(self):
		i = 0
		if(self.table[i][1] == 1):
			i = i+1
			return True
		else:
			return False
		

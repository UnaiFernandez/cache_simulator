
class Cache:
	def __init__(self, sword, sblock, sset, rpol, ad, rewr, hit, table,access):
		self.sword = sword
		self.sblock = sblock
		self.sset = sset
		self.rpol =rpol
		self.ad = ad
		self.rewr = rewr
		self.hit = hit
		self.table = table
		self.access = access

	def word(self):
		return self.ad//self.sword

	def number_blocks(self):
		return self.sblock//self.sword

	def number_words_block(self):
		return self.sblock//self.sword

	def number_words(self):
		return self.number_blocks()*self.number_words_block()

	def block(self):
		return self.word()//self.number_words_block()

	def number_sets(self):
		return 8//self.sset

	def set(self):
		if(self.sset == 8):
			return 0
		elif(self.sset == 1):
			return self.line()
		else:
			return self.block()%self.number_sets()

	def tag(self):
		if(self.sset == 8):
			return self.block()
		elif(self.sset == 1):
			return self.block()//self.number_lines()
		else:
			return self.block()//self.number_sets()

	def number_lines(self):
		return 8

	def line(self):
		return self.block()%self.number_lines() 

	def hit_miss(self):
		for i in range(len(self.table)):
			if(self.table[i][4] == self.block()):
				return True
		return(self.table[i][4] == self.block())

	def hits(self):
		if(self.hit_miss() == True):
			self.hit += 1
		if(self.hit > 2):
			self.hit -= 1
		return self.hit
			
	def hit_rate(self):
		return self.hits()/self.access

	def dirty(self):
		i = 0
		if(self.rewr == 1):
			i = i+1
			return True
		elif(self.rewr == 0):
			return False
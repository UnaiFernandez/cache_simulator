
class Cache:
	def __init__(self, sword, sblock, sset, rpol, ad, rewr, hit, table,access):
		self.sword = sword #word size
		self.sblock = sblock #block size
		self.sset = sset #set size
		self.rpol =rpol #replacement policy
		self.ad = ad #address
		self.rewr = rewr #read or write
		self.hit = hit #hit or miss (boolean)
		self.table = table
		self.access = access #number of accesses

	#Calculates the word
	def word(self):
		return self.ad//self.sword

	#Calculates the number of blocks
	def number_blocks(self):
		return self.sblock//self.sword

	#Calculates the number of words in a block
	def number_words_block(self):
		return self.sblock//self.sword

	#calculates the number of words
	def number_words(self):
		return self.number_blocks()*self.number_words_block()

	#Calculates the block
	def block(self):
		return self.word()//self.number_words_block()

	#Calculates the number of sets
	def number_sets(self):
		return 8//self.sset

	#calculates the set
	def set(self):
		if(self.sset == 8):
			return 0
		elif(self.sset == 1):
			return self.line()
		else:
			return self.block()%self.number_sets()

	#calculates the tag
	def tag(self):
		if(self.sset == 8):
			return self.block()
		elif(self.sset == 1):
			return self.block()//self.number_lines()
		else:
			return self.block()//self.number_sets()

	#calculates the number of lines
	def number_lines(self):
		return 8

	#calculates the line
	def line(self):
		return self.block()%self.number_lines() 

	#the function determines if there is a hit or not
	def hit_miss(self):
		for i in range(len(self.table)):
			if(self.table[i][4] == self.block()):
				return True
		return(self.table[i][4] == self.block())

	#counts the hits
	def hits(self):
		if(self.hit_miss() == True):
			self.hit += 1
		if(self.hit > 2):
			self.hit -= 1
		return self.hit
			
	#calculates the hit rate
	def hit_rate(self):
		return self.hits()/self.access

	#the function determines if the value you entered is dirty
	def dirty(self):
		i = 0
		if(self.rewr == 1):
			i = i+1
			return True
		elif(self.rewr == 0):
			return False
class Cache:
	def __init__(self, sword, sblock, sset, rpol, ad, rewr):
		self.sword = sword
		self.sblock = sblock
		self.sset = sset
		self.rpol =rpol
		self.ad = ad
		self.rewr = rewr

	def word(self):
		return self.ad//self.sword

	def number_blocks(self):
		return self.sblock//self.sword

	def block(self):
		return self.word()//self.number_blocks()

	def number_sets(self):
		return 8//self.sset

	def set(self):
		return self.block()%self.number_sets()

	def tag(self):
		return self.word()//self.block()


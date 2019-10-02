class Setfifo:
	def __init__(self, sset, line, setnum , dirty, tag, block, hit, table):
			self.sset = sset
			self.line = line
			self.setnum = setnum
			self.dirty = dirty
			self.tag = tag
			self.block = block
			self.hit = hit
			self.table = table

	def repl(self, i):
		return self.table[i][3]

	def intdirty(self):
		if(self.dirty == True):
			return 1
		elif(self.dirty == False):
			return 0

	def replace(self,i):
		self.table[i][0] = 1
		self.table[i][1] = self.intdirty()
		self.table[i][2] = self.tag
		self.table[i][3] = -1
		self.table[i][4] = self.block


	def finder(self):
		if(self.hit == True):	
			for i in range(len(self.table)):
				if(self.table[i][2] == self.tag):
					self.replace(i)
					i = 1
					while(i < 9):
						if(self.table[i][3] != 8):
							self.table[i][3] = i
						else:
							i = 1
							self.table[i][3] = i
						i = i + 1
		else:
			if(self.sset == 1):	
				self.table[self.line][0] = 1
				self.table[self.line][1] = self.intdirty()
				self.table[self.line][2] = self.tag
				self.table[self.line][3] = -1
				self.table[self.line][4] = self.block
				i = 0
				while(i < 9):
					if(self.table[i][3] == 8):
						i = 0
						self.table[i][3] = i+1
					else:
						self.table[i][3] = i+1
					
			elif(self.sset == 2):
				print("yeet")

			#elif(self.sset == 4):

			#elif(self.sset == 8):	
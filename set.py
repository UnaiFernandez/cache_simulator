
class Set:
	def __init__(self, sset, line, setnum , dirty, tag, block, table):
			self.sset = sset
			self.line = line
			self.setnum = setnum
			self.dirty = dirty
			self.tag = tag
			self.block = block
			self.table = table

	def repl(self, i):
		return self.table[i][3]

	def intdirty(self):
		if(self.dirty == True):
			return 0
		elif(self.dirty == False):
			return 1

	def replace(self,i):
		self.table[i][0] = 1
		self.table[i][1] = self.intdirty()
		self.table[i][2] = self.tag
		self.table[i][3] = -1
		self.table[i][4] = self.block


	def finder(self):
		if(self.sset == 1):	
			self.table[self.line][0] = 1
			self.table[self.line][1] = self.intdirty()
			self.table[self.line][2] = self.tag
			self.table[self.line][3] = -1
			self.table[self.line][4] = self.block
			for i in range(len(self.table)):
				if(self.table[i][3] > 0):
					self.table[i][3] += 1 
				elif(self.table[i][3] == -1):
					self.table[i][3] = 1

		elif(self.sset == 2):
			found = False
			if(self.setnum == 0):
				for i in range(0,2):
					if(found == False):
						if(self.repl(i) == 0):
							self.replace(i)
							found = True
						elif(self.repl(i) == 2):
							self.replace(i)
							found = True
					if(self.table[i][3] > 0):
						self.table[i][3] += 1 
					elif(self.table[i][3] == -1):
						self.table[i][3] = 1
			elif(self.setnum == 1):
				for i in range(2,4):
					if(found == False):
						if(self.repl(i) == 0):
							self.replace(i)
							found = True
						elif(self.repl(i) == 2):
							self.replace(i)
							found = True
					if(self.table[i][3] > 0):
						self.table[i][3] += 1 
					elif(self.table[i][3] == -1):
						self.table[i][3] = 1
			elif(self.setnum == 2):
				for i in range(4,6):
					if(found == False):
						if(self.repl(i) == 0):
							self.replace(i)
							found = True
						elif(self.repl(i) == 2):
							self.replace(i)
							found = True
					if(self.table[i][3] > 0):
						self.table[i][3] += 1 
					elif(self.table[i][3] == -1):
						self.table[i][3] = 1
			elif(self.setnum == 3):
				for i in range(6,8):
					if(found == False):
						if(self.repl(i) == 0):
							self.replace(i)
							found = True
						elif(self.repl(i) == 2):
							self.replace(i)
							found = True
					if(self.table[i][3] > 0):
						self.table[i][3] += 1 
					elif(self.table[i][3] == -1):
						self.table[i][3] = 1
		elif(self.sset == 4):
			found = False
			if(self.setnum == 0):
				for i in range(0,4):
					if(found == False):
						if(self.repl(i) == 0):
							self.replace(i)
							found = True
						elif(self.repl(i) == 2):
							self.replace(i)
							found = True
					if(self.table[i][3] > 0):
						self.table[i][3] += 1 
					elif(self.table[i][3] == -1):
						self.table[i][3] = 1
			elif(self.setnum == 1):
				for i in range(4,8):
					if(found == False):
						if(self.repl(i) == 0):
							self.replace(i)
							found = True
						elif(self.repl(i) == 2):
							self.replace(i)
							found = True
					if(self.table[i][3] > 0):
						self.table[i][3] += 1 
					elif(self.table[i][3] == -1):
						self.table[i][3] = 1

		elif(self.sset == 8):	
			found = False
			for i in range(len(self.table)):
				if(found == False):
					if(self.repl(i) == 0):
						self.replace(i)
						found = True
					elif(self.repl(i) == 8):
						self.replace(i)
						found = True
				if(self.table[i][3] > 0):
					self.table[i][3] += 1 
				elif(self.table[i][3] == -1):
					self.table[i][3] = 1
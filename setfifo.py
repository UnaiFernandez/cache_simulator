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
		self.table[i][3] = 0
		self.table[i][4] = self.block


	def finder(self):
		if(self.hit == True):	
			for i in range(len(self.table)):
				if(self.table[i][2] == self.tag):
					self.replace(i)
					for i in range(0,8):
						if(self.table[i][3] == 8):
							i = 0
							self.table[i][3] = i+1
						else:
							self.table[i][3] = i+1
		else:
			if(self.sset == 1):	
				self.table[self.line][0] = 1
				self.table[self.line][1] = self.intdirty()
				self.table[self.line][2] = self.tag
				self.table[self.line][3] = -1
				self.table[self.line][4] = self.block
				if(self.table[self.line][3] == 8):
					self.table[self.line][3] = 1
				else:
					self.table[self.line][3] += 1
					
			elif(self.sset == 2):
				found = False
				full = False
				pop = False
				if(self.setnum == 0):
					fifo1 = 0
					for i in range(0,2):
						fifo1 = fifo1 + 1
						if(found == False):
							if(self.repl(i) == 0):
								self.table[i][0] = 1
								self.table[i][1] = self.intdirty()
								self.table[i][2] = self.tag
								self.table[i][3] = fifo1
								self.table[i][4] = self.block
								found = True
							elif(self.repl(i) == 2):
								self.table[i][0] = 1
								self.table[i][1] = self.intdirty()
								self.table[i][2] = self.tag
								self.table[i][3] = 2
								self.table[i][4] = self.block
								pop = True
							if(fifo1 == 2):
								full = True
					for j in range(0,2):
						if(full == True):
							if(self.repl(j) == 1):
								self.table[j][3] = 2
					if(pop == True):
						for x in range(0,2):
							self.table[x][3] -= 1
				elif(self.setnum == 1):
					fifo2 = 0
					for i in range(2,4):
						fifo2 = fifo2 + 1
						if(found == False):
							if(self.repl(i) == 0):
								self.table[i][0] = 1
								self.table[i][1] = self.intdirty()
								self.table[i][2] = self.tag
								self.table[i][3] = fifo2
								self.table[i][4] = self.block
								found = True
							elif(self.repl(i) == 3):
								self.table[i][0] = 1
								self.table[i][1] = self.intdirty()
								self.table[i][2] = self.tag
								self.table[i][3] = 3
								self.table[i][4] = self.block
								pop = True
							if(fifo2 == 2):
								full = True
					for j in range(2,4):
						if(full == True):
							if(self.repl(j) == 1):
								self.table[j][3] = 3
					if(pop == True):
						for x in range(2,4):
							self.table[x][3] -= 1
				elif(self.setnum == 2):
					fifo3 = 0
					for i in range(4,6):
						fifo3 = fifo3 + 1
						if(found == False):
							if(self.repl(i) == 0):
								self.table[i][0] = 1
								self.table[i][1] = self.intdirty()
								self.table[i][2] = self.tag
								self.table[i][3] = fifo3
								self.table[i][4] = self.block
								found = True
							elif(self.repl(i) == 2):
								self.table[i][0] = 1
								self.table[i][1] = self.intdirty()
								self.table[i][2] = self.tag
								self.table[i][3] = 2
								self.table[i][4] = self.block
								pop = True
							if(fifo3 == 2):
								full = True
					for j in range(4,6):
						if(full == True):
							if(self.repl(j) == 1):
								self.table[j][3] = 2
					if(pop == True):
						for x in range(4,6):
							self.table[x][3] -= 1
				elif(self.setnum == 3):
					fifo4 = 0
					for i in range(6,8):
						fifo4 = fifo4 + 1
						if(found == False):
							if(self.repl(i) == 0):
								self.table[i][0] = 1
								self.table[i][1] = self.intdirty()
								self.table[i][2] = self.tag
								self.table[i][3] = fifo4
								self.table[i][4] = self.block
								found = True
							elif(self.repl(i) == 2):
								self.table[i][0] = 1
								self.table[i][1] = self.intdirty()
								self.table[i][2] = self.tag
								self.table[i][3] = 2
								self.table[i][4] = self.block
								pop = True
							if(fifo4 == 2):
								full = True
					for j in range(6,8):
						if(full == True):
							if(self.repl(j) == 1):
								self.table[j][3] = 2
					if(pop == True):
						for x in range(6,8):
							self.table[x][3] -= 1

			elif(self.sset == 8):
				found = False
				fifo = 0
				full = False
				pop = False
				for i in range(len(self.table)):
					fifo = fifo + 1
					if(found == False):
						if(self.repl(i) == 0):
							self.table[i][0] = 1
							self.table[i][1] = self.intdirty()
							self.table[i][2] = self.tag
							self.table[i][3] = fifo
							self.table[i][4] = self.block
							found = True
						elif(self.repl(i) == 9):
							self.table[i][0] = 1
							self.table[i][1] = self.intdirty()
							self.table[i][2] = self.tag
							self.table[i][3] = 9
							self.table[i][4] = self.block
							pop = True
						if(fifo == 8):
							full = True
				for j in range(len(self.table)):
					if(full == True):
						if(self.repl(j) == 1):
							self.table[j][3] = 9
				if(pop == True):
					for x in range(len(self.table)):
						self.table[x][3] -= 1
							
									  	
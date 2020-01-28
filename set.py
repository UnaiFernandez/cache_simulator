class Set:
	def __init__(self, sset, line, setnum , dirty, tag, block, hit, table):
			self.sset = sset #set size
			self.line = line #line
			self.setnum = setnum #set number
			self.dirty = dirty 
			self.tag = tag 
			self.block = block
			self.hit = hit #hit or miss (boolean)
			self.table = table

	#this function the value of the replacement number
	def repl(self, i):
		return self.table[i][3]

	#this function return 1 if the entered value is dirty
	def intdirty(self):
		if(self.dirty == True):
			return 1
		elif(self.dirty == False):
			return 0

	#as in most of the cases this are the changes to make, this function makes the code shorter and more readable
	def replace(self,i):
		self.table[i][0] = 1
		self.table[i][1] = self.intdirty()
		self.table[i][2] = self.tag
		self.table[i][3] = -1
		self.table[i][4] = self.block


	#this function replaces the values and changes the replacement bit
	def finder(self):
		#the steps to follow if there is a hit
		if(self.hit == True):	
			for i in range(len(self.table)):
				if(self.table[i][2] == self.tag):
					self.replace(i)
					if(self.table[i][3] > 0):
						self.table[i][3] += 1 
					elif(self.table[i][3] == -1):
						self.table[i][3] = 1
		#the steps to follow if there is a miss
		else:
			#if the set size is 1 (direct mapped)
			if(self.sset == 1):	
				#inserts the values in the table
				self.table[self.line][0] = 1
				self.table[self.line][1] = self.intdirty()
				self.table[self.line][2] = self.tag
				self.table[self.line][3] = -1
				self.table[self.line][4] = self.block
				#updates the replacement numbers
				for i in range(len(self.table)):
					if(self.table[i][3] > 0):
						self.table[i][3] += 1 
					elif(self.table[i][3] == -1):
						self.table[i][3] = 1

			#if the set size is 2 (set associative)	
			elif(self.sset == 2):
				found = False
				#inserts the values in the table
				if(self.setnum == 0):
					for i in range(0,2):
						if(found == False):
							if(self.repl(i) == 0):
								self.replace(i)
								found = True
							elif(self.repl(i) == 2):
								self.replace(i)
								found = True
						#updates the replacement numbers
						if(self.table[i][3] > 0):
							self.table[i][3] += 1 
						elif(self.table[i][3] == -1):
							self.table[i][3] = 1
				elif(self.setnum == 1):
					#inserts the values in the table
					for i in range(2,4):
						if(found == False):
							if(self.repl(i) == 0):
								self.replace(i)
								found = True
							elif(self.repl(i) == 2):
								self.replace(i)
								found = True
						#updates the replacement numbers
						if(self.table[i][3] > 0):
							self.table[i][3] += 1 
						elif(self.table[i][3] == -1):
							self.table[i][3] = 1
				elif(self.setnum == 2):
					#inserts the values in the table
					for i in range(4,6):
						if(found == False):
							if(self.repl(i) == 0):
								self.replace(i)
								found = True
							elif(self.repl(i) == 2):
								self.replace(i)
								found = True
						#updates the replacement numbers
						if(self.table[i][3] > 0):
							self.table[i][3] += 1 
						elif(self.table[i][3] == -1):
							self.table[i][3] = 1
				elif(self.setnum == 3):
					#inserts the values in the table
					for i in range(6,8):
						if(found == False):
							if(self.repl(i) == 0):
								self.replace(i)
								found = True
							elif(self.repl(i) == 2):
								self.replace(i)
								found = True
						#updates the replacement numbers
						if(self.table[i][3] > 0):
							self.table[i][3] += 1 
						elif(self.table[i][3] == -1):
							self.table[i][3] = 1
			

			#if the set size is 4 (set associative)	
			elif(self.sset == 4):
				found = False
				if(self.setnum == 0):
					#inserts the values in the table
					for i in range(0,4):
						if(found == False):
							if(self.repl(i) == 0):
								self.replace(i)
								found = True
							elif(self.repl(i) == 2):
								self.replace(i)
								found = True
						#updates the replacement numbers
						if(self.table[i][3] > 0):
							self.table[i][3] += 1 
						elif(self.table[i][3] == -1):
							self.table[i][3] = 1
				elif(self.setnum == 1):
					#inserts the values in the table
					for i in range(4,8):
						if(found == False):
							if(self.repl(i) == 0):
								self.replace(i)
								found = True
							elif(self.repl(i) == 2):
								self.replace(i)
								found = True
						#updates the replacement numbers
						if(self.table[i][3] > 0):
							self.table[i][3] += 1 
						elif(self.table[i][3] == -1):
							self.table[i][3] = 1

			
			#if set size is 8 (fully associative)
			elif(self.sset == 8):	
				found = False
				#inserts the values in the table
				for i in range(len(self.table)):
					if(found == False):
						if(self.repl(i) == 0):
							self.replace(i)
							found = True
						elif(self.repl(i) == 8):
							self.replace(i)
							found = True
					#updates the replacement numbers
					if(self.table[i][3] > 0):
						self.table[i][3] += 1 
					elif(self.table[i][3] == -1):
						self.table[i][3] = 1

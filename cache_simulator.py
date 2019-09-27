import math
from cache import Cache
from set import Set
from timee import Time


print("")
print("           ###########################################################")
print("           ###################   CACHE SIMULATOR   ###################")
print("           ###########################################################")
print("")
print("")
print("")
print("choose options:")
print("")
ws = int(input("word size (bytes): 4 - 8  ---------------> ")) 
bls = int(input("Block/Line size (bytes): 32 - 64  -------> "))
ss = int(input("Set size (lines): 1 - 2 - 4 - 8  --------> "))
Rpol = int(input("Replacement pol.: FIFO (0) - LRU (1)  ---> "))
print("")
table = [[0,0,0,0,"---"],
		[0,0,0,0,"---"],
		[0,0,0,0,"---"],
		[0,0,0,0,"---"],
		[0,0,0,0,"---"],
		[0,0,0,0,"---"],
		[0,0,0,0,"---"],
		[0,0,0,0,"---"]]
exit = False
access = 1
i = 0
while(exit == False & i<=7):
	ad = int(input("Mem. address (byte)  --------------------> "))
	loadstore = int(input("read (0) - Write (1)  -------------------> "))

	c = Cache(ws,bls,ss,Rpol,ad,loadstore,table,access)
	
	print("")
	print("")
	print("")
	print("Address: " + str(ad) + " / Word: " + str(c.word()) + " / Block: " + str(c.block()))
	print("Set: " + str(c.set()) + " / Tag: " + str(c.tag()))

	s = Set(c, table)
	t = Time(c.rewr, c.hit_miss(),c.dirty(),c.number_words_block())

	print(str(c.hit_miss()))
	print("Access time: " + str(t.accesstime()))
	print("Hit rate: " + str(c.hit_rate()))


	if(ss == 8):
		full = False
		if(i == 7):
			table[i][2] = tag
			if(loadstore == 1):
				table[i][1] = 1
			if(loadstore == 0):
				table[i][1] = 0
			if(full == True):
				table[i][3] = 1
			full = True
			i = 0
		elif(i<7):
			table[i][2] = tag
			if(loadstore == 1):
				table[i][1] = 1
			if(loadstore == 0):
				table[i][1] = 0
			if(full == True):
				table[i][3] = 1
			i = i+1



	print("")
	print("")
	print("")
	print("| busy | dirty | tag | repl. || data |")
	print("--------------------------------------")

	for item in table:
		print("|",item[0]," "*(3-len(str(item[0]))),"|",item[1]," "*(4-len(str(item[1]))),"|",item[2]," "*(2-len(str(item[2]))),"|",item[3]," "*(4-len(str(item[3]))),"||",item[4]," "*(3-len(str(item[4]))),"|",)

	print("")
	print("")
	print("")

	a = input("Exit?  [y/n]")
	if(a == 'y'):
		exit = True
	else:
		exit = False

	access = access + 1
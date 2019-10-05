import math
from cache import Cache
from set import Set
from timee import Time
from setfifo import Setfifo



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
h = 0 #hit rate
i = 0
total_accesstime = 0
while(exit == False & i<=7):


	ad = int(input("Mem. address (byte)  --------------------> "))
	loadstore = int(input("read (0) - Write (1)  -------------------> "))

	c = Cache(ws,bls,ss,Rpol,ad,loadstore,h,table,access)
	
	print("")
	print("")
	print("")
	print("Address: " + str(ad) + " / Word: " + str(c.word()) + " / Block: " + str(c.block()))
	print("Set: " + str(c.set()) + " / Tag: " + str(c.tag()) + " / Line: " + str(c.line()))
	
	if(Rpol == 1):
		s = Set(ss, c.line(), c.set(), c.dirty(), c.tag(), c.block(), c.hit_miss(), table)
		t = Time(c.rewr, c.hit_miss(),c.dirty(),c.number_words_block(), table)

		print(str(c.hit_miss()))
		print(str(c.hits()))
		print(str(c.dirty()))
		h = c.hits()
		print("Access time: " + str(t.accesstime()))
		print("Hit rate: " + str(round(c.hit_rate(),2)))


		s.finder()


	if(Rpol == 0):
		sfifo = Setfifo(ss, c.line(), c.set(), c.dirty(), c.tag(), c.block(), c.hit_miss(), table)
		t = Time(c.rewr, c.hit_miss(),c.dirty(),c.number_words_block(), table)

		print("Hit: " + str(c.hit_miss()))
		print(str(c.hits()))
		h = c.hits()
		print("Access time: " + str(t.accesstime()))
		print("Hit rate: " + str(round(c.hit_rate(),2)))

		sfifo.finder()


	total_accesstime = total_accesstime + t.accesstime()
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
		print("Total access time: " + str(total_accesstime))
	else:
		exit = False

	access = access + 1
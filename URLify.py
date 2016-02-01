#given a string, replace all instances of spaces with '%20'

def URLify(s):
	newString = s.replace(' ','%20')
	return newString

def URLify2(s):
	space = '%20'
	list = s.split()
	return space.join(list)

#this implementation is redundant/not really useful -- more of an 
#emulation of what it would be like to implement this in a langauge 
#that does not involve such comprehensive string support
#def URLify3(s):
	#spaceCount = s.count(' ')
	#list = list(s)
	#list = [len(s)+3*spaceCount]
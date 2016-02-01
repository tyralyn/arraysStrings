#implementation of algorithm to determine whether string has all unique characters
#returns False if string is not comprised of unique characters, True otherwise

def isUnique(s):
	list=[]
	for i in range (0, len(s)):
		if s[i] in list:
			return False
		list.append(s[i])
	return True

def isUniqueDict(s):
	dict={}
	for i in range (0, len(s)):
		if s[i] in dict:
			return False;
		dict[s[i]] = 1
	return True;

def isUniqueNoDataStructures(s):
	for i in range (0, len(s)):
		if s[i] in s[i+1:]:
			return False
	return True


#Notes
#ask if string is unicode or ASCII 
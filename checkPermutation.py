#given two strings, determine whether one is a permutation of the other
#return false if not permutations, true otherwise

def checkPermutation(s1, s2):
	if len(s1)!=len(s2):
		return False
	d1 = {}
	d2 = {}
	for i in range (0, len(s1)):
		if s1[i] not in d1:
			d1[s1[i]]=1
		else:
			d1[s1[i]]=d1[s1[i]]+1
		if s2[i] not in d2:
			d2[s2[i]]=1
		else:	
			d2[s2[i]]=d2[s2[i]]+1
	return d1==d2

def checkPermutation2(s1, s2):
	list1 = list(s1)
	for i in range (0, len(s2)):
		if s2[i] in list1:
			list1.remove(s2[i])
		else:
			return False;
	return(len(list1) == 0)



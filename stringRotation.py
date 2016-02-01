#using a substring/contains method, determine whether a situation like 
#'waterbottle'->'erbottlewat' is going on. only use the substring method once

def stringRotation(s1, s2):
	doubles2 = s2+s2
	doubles1 = s1+s1
	return (s2 in doubles1 and s1 in doubles2)

#to do it with only one call to the substring/contains method
def stringRotation2(s1, s2):
	doubles1 = s1+s1
	if len(s1) == len(s2) and len(s1)!=0 and len(s2)!=0:
		return (s2 in doubles1)
	else:
		return false
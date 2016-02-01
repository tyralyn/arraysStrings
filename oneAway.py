#assuming that the possible edits are inserting a character, removing a character, or replacing a character. 
#given two strings, determine whether they are one or zero edits away

def oneAway(s1, s2):
	#handle case of two identical strings
	if s1==s2:
		return True;
	#handle case of one string being more than one character longer than the other
	if (abs(len(s1)-len(s2))>1):
		return False
	#handle the case of one string being one character longer than the other
	#figure out which string is longer, if any, and assign to the appropriate variable
	if len(s1) < len(s2):
		big = s2
		small = s1
	else:
		small = s2
		big = s1

	oneEdit = False 
	i = 0 #iterator for larger string
	for j in range (0, len(small)): #iterate through smaller string
		if big[i] == small[j]: #if the chars we are comparing are the same, continue
			i+=1
		else:
			#if we've already recorded an edit/a discrepancy, then return false
			if oneEdit == True:
				return False;
			oneEdit = True;
			#otherwise, this is the first difference we see
			if (len(small) == len(big)):
				i+=1
			else:
				i+=2
	return True

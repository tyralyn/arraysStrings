#given a string, check to see if it is a permutation of a palindrome
#q: is it space sensitive? case-sensitive? a: case-insensitive
#q: are spaces and non-letter characters involved? a: no. skip those
# a string like 'taCo c$at' would yield True, since the space and $ are ignored and the algorithm is case-insensitive

def palindromePermutation(s):
	list=[]
	for i in range (0, len(s)):
		if (not(ord('a') < ord(s[i]) < ord('z'))) and (not(ord('A') < ord(s[i]) < ord('Z'))):
			continue
		lowercaseLetter=s[i].lower()
		if lowercaseLetter not in list:
			list.append(lowercaseLetter)
		else:
			list.remove(lowercaseLetter)
	if len(list)>1:
	 	return False
	return True
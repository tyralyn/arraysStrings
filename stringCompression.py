#basic string compression of the form 'aaaabbcccccaa' -> 'a4b2c5a2'
#if the resulting string is less space efficient than the original, return the original
#assume only uppercase and lowercase letters

def stringCompression(s): 
	currentLetter = s[0];
	currentCount = 0;
	resultString=''
	for i in range (0, len(s)):
		if s[i]==currentLetter:
			currentCount+=1
		else:
			resultString+=currentLetter
			resultString+=str(currentCount)
			currentLetter=s[i]
			currentCount=1
	resultString+=currentLetter
	resultString+=str(currentCount)
	return (resultString if len(resultString)<len(s) else s)
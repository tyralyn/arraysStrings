def isPalindrome(s):
	for i in range (0, len(s)//2):
		if s[i]!=s[-(i+1)]:
			return False
	return True

def isPalindromeLinkedListSim(s):
	l = []
	for i in range(0, (len(s)//2 if len(s)%2==0 else (len(s)//2+1))):
		l.append(s[i])
	for i in range(len(s)//2, len(s)):
		if l.pop()!=s[i]:
			return False
	return True


		
palindromes = []
final = 0

def isPalindrome(s):
	isP = True
	c = lambda a,b:-(-a//b)
	for i in range(0,c(len(s),2)):
		if not s[i] == s[len(s)-i-1]:
			isP = False
			break
	return isP

for i in range(100,999):
	for j in range(100,999):
		if isPalindrome(str(i*j)):
			palindromes.append(i*j)

for n in palindromes:
	if n > final:
		final = n

print(final)
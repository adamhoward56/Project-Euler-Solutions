prime = []
factors = []

def generatePrime():
	for i in range(2,10000):
		p = True
		for x in range(2, i-1):
			if i % x == 0:
				p = False

		if p == True:
			prime.append(i)

def getPrimeFactor(x):
	f = []
	num = x
	i = 0
	while i < len(prime):
		if num == prime[i]:
			f.append(prime[i])
		if num % prime[i] == 0 and prime[i] < num:
			f.append(prime[i])
			num = num/prime[i]
		else:
			i = i + 1
	print f

generatePrime()
getPrimeFactor(600851475143)
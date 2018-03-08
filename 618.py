fib = []
#factors = []
total = 0
prime = []
sums = []
# Generate given number of Fibonacci numbers
def generateFib():
	for i in range (0,22):
		s = 0
		if (len(fib) == 0):
			fib.append(1)
		fib.append(fib[i-1] + fib[i])

def generatePrime():
	for i in range(2,522):
		p = True
		for x in range(2, i-1):
			if i % x == 0:
				p = False

		if p == True:
			prime.append(i)

def getPrimeFactorSum(x):
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
	#factors.append(f)

	s = 0
	#for i in # Finish this line 
	
def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors
    
# Start the program
def init():
	generateFib()
	print("\nFibonacci Numbers: " + str(fib))
	generatePrime()
	print("\nPrime Numbers: " + str(prime))
	d = 0
	while d <= 2**23184:
		sums.append(sum(prime_factors(d)))
		d = d + 1
	u = 0
	while u <= len(fib):
		e = 0
		while e <= len(sums):
			if sums[e] == fib[u]:
				total = total + sums[e]


init()

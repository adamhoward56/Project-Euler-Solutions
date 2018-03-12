<<<<<<< HEAD
#
# Project Euler problem 618, with contributions from Bennett Yardley & Brett Coury
#
import primefac

fib = [1,1]
primes = []

# Generates given amount of Fibonacci numbers
def generateFib():
	fib_count = 24
	for i in range (1,fib_count-1):
=======
fib = []
#factors = []
prime = []
sums = []
# Generate given number of Fibonacci numbers
def generateFib():
	for i in range (0,22):
>>>>>>> 8b9ecea05e11f875b29b5b1f5ee69b2b1c66bb9a
		s = 0
		fib.append(fib[i-1] + fib[i])

<<<<<<< HEAD
def generatePrimes():
	for i in range(0, 46368):
		ilist = list(primefac.primefac(i))
		if (len(ilist)) == 1:
			primes.append(sum(ilist))

=======
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
    
>>>>>>> 8b9ecea05e11f875b29b5b1f5ee69b2b1c66bb9a
# Start the program
def init():
	generateFib()
	generatePrimes()
	
	print("\nFibonacci Numbers: " + str(fib))
<<<<<<< HEAD
	print("\nPrime Numbers: " + str(primes))
	
	print("")
=======
	generatePrime()
	print("\nPrime Numbers: " + str(prime))
	d = 0
	while d <= 2**23184:
		sums.append(sum(prime_factors(d)))
		d = d + 1
	u = 0
	total = 0
	while u <= len(fib)-1:
		e = 0
		while e <= len(sums)-1:
			if sums[e] == fib[u]:
				total = total + e
			e = e + 1
		u = u + 1
	print(total)

>>>>>>> 8b9ecea05e11f875b29b5b1f5ee69b2b1c66bb9a

init()

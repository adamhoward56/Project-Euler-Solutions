#
# Project Euler problem 618, with contributions from Bennett Yardley & Brett Coury
#

fib = []
prime = []

# Generates given amount of Fibonacci numbers
def generateFib():
	fib_count = int(input("Enter the number of fibonacci numbers to include: "))
	for i in range (0,fib_count):
		s = 0
		if (len(fib) == 0):
			fib.append(1)
		fib.append(fib[i-1] + fib[i])

# Generate an array of prime numbers
def generatePrime():
	for i in range(2,522):
		p = True
		for x in range(2, i-1):
			if i % x == 0:
				p = False

		if p == True:
			prime.append(i)

# Returns the sum of the prime factors of a given number
def getPrimeFactorSum(x):
	f = []
	num = x
	i = 0
	s = 0
	while i < len(prime):
		if num == prime[i]:
			f.append(prime[i])
		if num % prime[i] == 0 and prime[i] < num:
			f.append(prime[i])
			num = num/prime[i]
		else:
			i = i + 1
	for e in f:
		s = s + e

	return s

# Start the program
def init():
	generateFib()
	print("\nFibonacci Numbers: " + str(fib))
	generatePrime()
	print("\nPrime Numbers: " + str(prime))

	print()

init()
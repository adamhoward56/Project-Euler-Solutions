fib = []
#factors = []
prime = []

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

# Start the program
def init():
	generateFib()
	print("\nFibonacci Numbers: " + str(fib))
	generatePrime()
	print("\nPrime Numbers: " + str(prime))
	print(len(fib))
	print()

init()

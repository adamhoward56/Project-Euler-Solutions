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
		s = 0
		fib.append(fib[i-1] + fib[i])

def generatePrimes():
	for i in range(0, 46368):
		ilist = list(primefac.primefac(i))
		if (len(ilist)) == 1:
			primes.append(sum(ilist))



# Start the program
def init():
	generateFib()
	generatePrimes()
	
	print("\nFibonacci Numbers: " + str(fib))
	print("\nPrime Numbers: " + str(primes))
	
	print("")

init()
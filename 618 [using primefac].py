import primefac
import gmpy2

fib = []
sums = []

def generateFib():
	for i in range (0,22):
		s = 0
		if (len(fib) == 0):
			fib.append(1)
		fib.append(fib[i-1] + fib[i])

def __main__():
	generateFib()
	print("Fibonacci Numbers: " + str(fib))
	d = 0
	while d <= 2**23184:
		sums.append(sum(list(primefac.primefac(d))))
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

__main__()

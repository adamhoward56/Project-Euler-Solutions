fib = [1,1]
s = 0
while fib[len(fib)-1] < 4000000:
	fib.append(fib[len(fib)-1] + fib[len(fib)-2])

for i in range(0,len(fib)-1):
	if fib[i] % 2 == 0:
		s = s + fib[i]

print(s)
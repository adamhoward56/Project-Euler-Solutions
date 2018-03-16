n = 20
stop = False
while not stop:
	for i in range(3,21):
		if not n%i==0: break
		if i==20: stop = True
	if not stop: n=n+20
print n
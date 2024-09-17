def nfact(n):
	if n==0:
		return 1
	else:
		return n*nfact(n-1)
a=int(input())
if a<0:
	print("Not possible")
else:
	print(nfact(a))

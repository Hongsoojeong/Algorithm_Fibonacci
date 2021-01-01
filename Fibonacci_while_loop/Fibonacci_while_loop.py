def fibo(n):
	if (n==0):
		return 1
	a=0
	b=1
	c=a+b
	while(n>0):
		c=a+b
		a=b
		b=c
		n=n-1
	return c
n=int(input())
print(fibo(n))


def gcd(a,b):
	while(a!=0 and b!=0):
		if(a>=b):
			a = a%b
		else:
			b = b%a
	if(a>=b):
		return a
	else:
		return b

x = eval(input("1 "))
y = eval(input("2 "))
print(gcd(x,y))
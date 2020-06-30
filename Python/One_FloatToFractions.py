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

def main():
	numerator = None
	while numerator==None:
		try:
			denominator = 1
			numerator = eval(input())
			while numerator!=0:
				if(numerator<0 or numerator>int(numerator)):
					denominator *=10
					numerator*=10
				else:

					Gcd = gcd(numerator,denominator)
					print(str(int(int(numerator)/Gcd))+"/"+str(int(int(denominator)/Gcd)),end='')
					print()
					numerator = None
					break
		except:
			numerator = None
main()
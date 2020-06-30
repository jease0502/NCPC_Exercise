def conunt(a,b,c):
	up = a*b+a*c+b*c
	down = a*b*c
	return up/down

import time
need = int(input("need:  "))
tStart = time.time()#計時開始
for i in range(1,2001):
	for j in range(1,2001):
		for k in range(1,2001):
			if(i>=j and j>=k):
				x = conunt(i,j,k)
				if(1/need == x):
					print(i,j,k)
tEnd = time.time()
print("It cost %f sec" % (tEnd - tStart))#會自動做近位

'''
3的時候數值
9 9 9
12 8 8
12 12 6
15 10 6
15 15 5
18 9 6
20 12 5
21 7 7
24 8 6
24 24 4
28 21 4
30 10 5
30 20 4
36 18 4
42 7 6
45 9 5
48 16 4
60 15 4
84 14 4
120 8 5
156 13 4

2的時候數值
6 6 6
8 8 4
10 5 5
12 6 4
12 12 3
15 10 3
18 9 3
20 5 4
24 8 3
42 7 3

1的時候數值
3 3 3
4 4 2
6 3 2
'''
n=int(input())
for j in range(n):
    length=int(input())
    l=list(map(int,input().split()))
    a=l.count(l[0])
    if a==1:
        print(1)
    else:
        for i in range(0,length):
            if l[i]!=l[0]:
                print(i+1)
                breakn = int(input())
a = [i for i in map(int, input().split(' '))]
if sum(a) != 0:
	print('YES')
	print(1)
	print(1, n)
else:
	if a == [0] * len(a):
		print('NO')
	else:
		print('YES')
		c = 0
		i = 0
		while c == 0:
			c += a[i]
			i += 1
		print(2)
		print(1, i)
		print(i + 1, n)
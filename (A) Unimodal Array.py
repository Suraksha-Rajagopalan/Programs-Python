end=int(input())
l=list(map(int,input().split()))
i = 1
while i < end and l[i - 1] < l[i]:
    i += 1
while i < end and l[i - 1] == l[i]:
    i += 1
while i < end and l[i - 1] > l[i]:
    i += 1
if i==end:
    print('YES')
else:
    print('NO')
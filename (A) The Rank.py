n=int(input())
for i in range(0,n):
    a=list(map(int,input().split()))
    sum=0
    for b in a:
        sum+=b
    if i==0:
        thomas=sum
        r=1
    if sum>thomas:
        r+=1
print(r)
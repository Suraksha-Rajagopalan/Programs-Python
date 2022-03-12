n=int(input())
for i in range(n):
    a,b,c,d=map(int,input().split())
    sum=a+b+c+d
    if i==0:
        thomas=sum
        rank=1
    if sum>thomas:
        rank+=1
print(rank)
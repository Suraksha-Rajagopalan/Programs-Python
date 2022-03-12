t=int(input())
count=0
for i in range(t):
   sum=0
   a,b,c=map(int,input().split())
   sum=a+b+c
   if sum>=2:
      count+=1
print(count)
n,k=map(int,input().split())
count=0
start=0
r=[]
for i in range(k+1):
    r+=str(i)
if k==0:
    start=1
for i in range(n):
    s=input()
    l=r.copy()
    for i in range(start,len(s)):
        if s[i] in l:
            l.remove(s[i])
    if l==[]:
        count+=1
print(count)
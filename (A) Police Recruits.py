n=input()
l=list(map(int,input().split()))
c=0
p=0
n=len(l)
for i in range(n):
    if l[i]!=-1:
        p+=l[i]
    else:
        if p>0:
            p-=1
        else:
            c+=1
print(c)
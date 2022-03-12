n=int(input())
string=input()
d={}
for i in range(0,n):
    if i!=n-1:
        if string[i]+string[i+1] not in d:
            d[string[i]+string[i+1]]=1
        else:
            d[string[i]+string[i+1]]+=1
max=0
for i in d:
    if d[i]>max:
        max=d[i]
        s=i
print(s)
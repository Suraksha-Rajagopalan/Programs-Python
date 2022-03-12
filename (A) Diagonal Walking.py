n=int(input())
s=input()
a=''
i=0
while i<n:
    if i!=n-1:
        if (s[i]+s[i+1]=='UR' or s[i]+s[i+1]=='RU'):
            a+='D'
            i+=1
        else:
            a+=s[i]
    elif i==n-1:
        if (s[i]+s[i-1]!='UR' or s[i]+s[i-1]!='RU'):
            a+=s[i]
    i+=1
print(len(a))
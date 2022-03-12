s=input().lower()
b=s[::-1]
if s==b:
    if len(s)%2==0:
        print('NO')
    else:
        print('YES')
else:
    c=0
    for i in range(0,len(s)//2):
        if s[i]!=s[-(i+1)]:
            c+=1
    if c==1:
        print('YES')
    else:
        print('NO')
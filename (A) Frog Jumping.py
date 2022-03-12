t=int(input())
for i in range(t):
    a,b,k=map(int,input().split())
    x=0
    if a==b:
        if k%2==0:
            print(0)
            continue
        else:
            print(b)
            continue
    if k%2==0:
        x=(a*(k//2))-(b*(k//2))
    else:
        x=((a*((k+1)//2))-(b*((k+1)//2)))+b
    print(x)
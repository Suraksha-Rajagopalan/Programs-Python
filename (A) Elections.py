t=int(input())
for i in range(t):
    a,b,c=map(int,input().split())
    x=max(b,c)-a+1
    y=max(a,c)-b+1
    z=max(a,b)-c+1
    if x<0:
        x=0
    elif y<0:
        y=0
    elif z<0:
        z=0
    print(x,y,z)
a,b,c=map(int,input().split())
if a>=b and a>=c:
    high=a
    x=b
    y=c
elif b>=a and b>=c:
    high=b
    x=a
    y=c
elif c>=b and c>=a:
    high=c
    x=a
    y=b
if high!=0:
    if high<x+y:
        print(0)
    else:
        ans=(high-(x+y))+1
        print(ans)
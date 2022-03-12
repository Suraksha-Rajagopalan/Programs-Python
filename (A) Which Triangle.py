t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    c=180-(a+b)
    if a==b and b==c:
        print('equilateral')
    elif a==b or b==c or c==a:
        print('isosceles')
    else:
        print('scalene')
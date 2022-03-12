match=int(input())
x=list(input().split())
y=list(input().split())
for i in range(0,match):
    if int(y[i])!=int(x[i])+10:
        print(x[i],end=' ')
        print(y[i])
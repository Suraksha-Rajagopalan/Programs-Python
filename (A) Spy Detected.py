n=int(input())
for j in range(n):
    length=int(input())
    l=list(map(int,input().split()))
    a=l.count(l[0])
    if a==1:
        print(1)
    else:
        for i in range(0,length):
            if l[i]!=l[0]:
                print(i+1)
                break
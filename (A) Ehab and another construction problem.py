n=int(input())
count=0
for i in range(2,n+1):
    for j in range(2,i+1):
        if i%j==0 and i*j>n and i/j<n:
            count+=1
            print(i,j)
            break
    if count>0:
        break
if count==0:
    print(-1)
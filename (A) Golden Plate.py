w,h,rings=map(int,input().split())
if w<3 or h>100 or rings>(min(w,h)+1)//2:
    print("Error!!")
else:
    r,sum=0,0
    for i in range(rings):
        sum+=(((w-r)*2)+((h-r)*2))-4
        r+=4
    print(sum)
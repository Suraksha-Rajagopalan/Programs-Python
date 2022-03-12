a=input()
count=0
for i in a:
    if 'a'==i:
        count+=1
if count>len(a)//2:
    print(len(a))
else:
    print((count*2)-1)
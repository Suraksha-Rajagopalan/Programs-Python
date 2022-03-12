a=input()
d,count={},0
for i in a:
    if i not in d:
        d[i]=1
        count+=1
    else:
        d[i]+=1
if count%2==0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')
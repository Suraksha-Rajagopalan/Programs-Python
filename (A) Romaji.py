a=input()
count=0
vowels='aeiou'
for i in range(0,len(a)):
    if a[i] not in vowels and i!=len(a)-1:
        if a[i+1] in vowels or a[i]=='n':
            count+=0
        else:
            count+=1
    if i==len(a)-1 and a[i] not in vowels and a[i]!='n':
        count+=1
if count==0:
    print('YES')
else:
    print('NO')
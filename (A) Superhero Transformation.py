s=input()
t=input()
ls,lt=len(s),len(t)
vowels='aeiou'
count=0
if ls!=lt:
    print('NO')
else:
    for i in range(0,len(s)):
        if s[i] in vowels and t[i] in vowels:
            count+=1
        if s[i] not in vowels and t[i] not in vowels:
            count+=1
    if count==ls:
        print('YES')
    else:
        print('NO')
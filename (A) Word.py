lower,upper=0,0
a=input()
for i in a:
    if i.islower():
        lower+=1
    elif i.isupper():
        upper+=1
if upper>lower:
    print(a.upper())
else:
    print(a.lower())
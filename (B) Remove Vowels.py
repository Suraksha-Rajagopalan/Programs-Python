sr_str=input()
vowels='aeiou'
for i in sr_str:
    if i not in vowels:
        print(i,end='')
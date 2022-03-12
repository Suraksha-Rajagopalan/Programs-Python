def sorted(string):
    l=[]
    a=''
    for i in string:
        l.append(i)
    l.sort()
    for j in l:
        a+=j
    print(a)
    
#__main__
n=int(input())
for i in range(n):
    string=input()
    sorted(string)
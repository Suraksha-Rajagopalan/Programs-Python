n=int(input())
string=input()
i,a=0,1
new_string=''
while i<n:
    new_string+=string[i]
    i+=a
    a+=1
print(new_string)
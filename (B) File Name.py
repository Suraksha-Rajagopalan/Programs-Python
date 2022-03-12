def substring(string):
   l,sub=[],''
   string+='a'
   if string=='x'*(len(string)):
       l.append(string)
   else:
       for i in string:
           if i=='x':
               sub+=i
           else:
               l.append(sub)
               sub=''
   return l
n=int(input())
s=input()
a=0
x_string=substring(s)
for i in x_string:
    if (len(i)-2)>0:
        a+=(len(i)-2)
print(a)
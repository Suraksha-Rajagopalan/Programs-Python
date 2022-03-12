n=int(input())
for i in range(n):
    string=input()
    if string[:len(string)//2]==string[len(string)//2:]:
        print('yes')
    else:
        print('no')
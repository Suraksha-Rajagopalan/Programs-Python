a = int(input())
b = input()
for i in range(a-1):
    if b[i] > b[i+1]:
        print(b[:i]+b[i+1:])
        exit()
print(b[:a-1])
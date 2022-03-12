n = int(input())
l = list(input().split())
yellow=green=red=0
for i in range(n):
  if l[i]=="yellow" :
    yellow+=1
  elif l[i]=="red" :
    red+=1
  elif l[i]=="green" :
    green+=1
if red>yellow and red>green:
  print("apple")
elif yellow>red and yellow>green:
  print("banana")
elif green>red and green>yellow:
  print("guava")    
elif yellow==red or red==green or green==yellow:
  print("none")
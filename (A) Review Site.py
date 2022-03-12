n=int(input())
for j in range(n):
    length=int(input())
    l=list(map(int,input().split()))
    upvote,downvote=0,0
    for i in l:
        if i==1:
            upvote+=1
        elif i==2:
            downvote+=1
        else:
            upvote+=1
    print(upvote)
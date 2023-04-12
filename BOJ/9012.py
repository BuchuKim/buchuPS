import sys

n,k = map(int,sys.stdin.readline().split())
li = [i for i in range(1,n+1)]
index = -1
answer = []
while (len(li)>0):
    index += k
    if (index>=len(li)):
        while (index>=len(li)):
            index -= len(li)
    answer.append(li[index])
    del(li[index])
for i in answer:
    print(i,end=' ')
from sys import stdin
from collections import deque
T = int(stdin.readline())
def findIndex(Q,N):
    if (len(Q)==0):
        return 0
    start = 0
    end = len(Q)-1
    while (start<=end):
        mid = (start+end)//2
        if (Q[mid]>=N):
            end = mid - 1
        else:
            start = mid + 1
    return start
for _ in range(T):
    k = int(stdin.readline())
    q = deque()
    for _ in range(k):
        command = stdin.readline().split()
        if (command[0]=="I"):
            i = int(command[1])
            q.insert(findIndex(q,i),i)
        elif (command[0]=="D"):
            if (len(q)==0):
                continue
            if (command[1]=="-1"):
                q.popleft()
            else: #command[1]=="1"
                q.pop()
    if (len(q)==0):
        print("EMPTY")
    else:
        print(q[len(q)-1],q[0],sep=' ')
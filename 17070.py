import sys;read=sys.stdin.readline
from collections import deque
N = int(read())
graph = []
for _ in range(N):
    graph.append(list(map(int,read().split())))
# 0: 가로, 1: 세로, 2: 대각선
ans = 0
if (graph[-1][-1]==1):
    print(0)
    exit()
bfsQ = deque()
bfsQ.append([0,1,0])
while bfsQ:
    a,b,shape = bfsQ.popleft()
    if (a==N-1 and b==N-1):
        ans+=1
    if (shape==0):
        if (b+1<N and graph[a][b+1]!=1):
            bfsQ.append([a,b+1,0])
        if (a+1<N and b+1<N and graph[a+1][b]!=1 and graph[a][b+1]!=1 and graph[a+1][b+1]!=1):
            bfsQ.append([a+1,b+1,2])
    elif (shape==1):
        if (a+1<N and graph[a+1][b]!=1):
            bfsQ.append([a+1,b,1])
        if (a+1<N and b+1<N and graph[a+1][b]!=1 and graph[a][b+1]!=1 and graph[a+1][b+1]!=1):
            bfsQ.append([a+1,b+1,2])
    else:
        if (b+1<N and graph[a][b+1]!=1):
            bfsQ.append([a,b+1,0])
        if (a+1<N and graph[a+1][b]!=1):
            bfsQ.append([a+1,b,1])
        if (a+1<N and b+1<N and graph[a+1][b]!=1 and graph[a][b+1]!=1 and graph[a+1][b+1]!=1):
            bfsQ.append([a+1,b+1,2])
print(ans)
import sys;input=sys.stdin.readline
from itertools import combinations
from collections import deque
import copy
n,m = map(int,input().split())
graph = []
virus = []
for i in range(n):
    li = list(map(int,input().split()))
    for j in range(n):
        if li[j]==2:
            virus.append([i,j])
    graph.append(li)
dx = [-1,1,0,0]
dy = [0,0,-1,1]
ans = 10001
comb = combinations(virus,m)
for c in comb:
    lab = copy.deepcopy(graph)
    Q = deque()
    time = 0
    for v in c:
        lab[v[0]][v[1]] = -1
        Q.append([v[0],v[1],0])
    while Q:
        x,y,t = Q.popleft()
        changed = False
        if t>=ans:
            break
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if lab[nx][ny]==0:
                    changed = True
                    lab[nx][ny] = t+1
                    Q.append([nx,ny,t+1])
                elif graph[nx][ny]==2 and lab[nx][ny]!=-1:
                    lab[nx][ny] = -1
                    Q.append([nx,ny,t+1])
        if changed:
            time = t+1
    isDone = True
    for li in lab:
        if 0 in li:
            isDone = False
            break
    if isDone:
        if time==0:
            print(0)
            exit()
        else:
            ans = min(ans,time)
if ans>10000:
    print(-1)
else:
    print(ans)
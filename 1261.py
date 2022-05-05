import sys;read=sys.stdin.readline
from collections import deque
m,n = map(int,read().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,list(read().rstrip()))))
bfsQ = deque([[0,0,0]])
destroyed = [[sys.maxsize for _ in range(m)] for _ in range(n)]
destroyed[0][0] = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def isWall(x,y):
    return 0<=x<n and 0<=y<m and graph[x][y]==1
def isValid(x,y):
    return 0<=x<n and 0<=y<m and graph[x][y]==0
while bfsQ:
    x,y,destroy = bfsQ.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if isWall(nx,ny):
            if (destroyed[nx][ny]>destroy+1):
                destroyed[nx][ny] = destroy+1
                bfsQ.append([nx,ny,destroy+1])
        elif isValid(nx,ny):
            if (destroyed[nx][ny]>destroy):
                destroyed[nx][ny] = destroy
                bfsQ.appendleft([nx,ny,destroy])
print(destroyed[-1][-1])
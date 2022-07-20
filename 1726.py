import sys;input=sys.stdin.readline
from collections import deque
m,n = map(int,input().split())
factory = []
for _ in range(m):
    factory.append(list(map(int,input().split())))
sx,sy,sd = map(int,input().split())
ex,ey,ed = map(int,input().split())

# 동쪽이 1, 서쪽이 2, 남쪽이 3, 북쪽이 4
def forward(x,y,d,k):
    if d==1:
        return x,y+k
    elif d==2:
        return x,y-k
    elif d==3:
        return x+k,y
    else:
        return x-k,y
def turnDir(d):
    if d==1 or d==2:
        return 3,4
    else:
        return 1,2
visited = [[[0 for _ in range(5)] for _ in range(n)] for _ in range(m)]
Q = deque()
Q.append([sx-1,sy-1,sd,0])
visited[sx-1][sy-1][sd] = 0
while Q:
    x,y,d,t = Q.popleft()
    if x==ex-1 and y==ey-1 and d==ed:
        print(t)
        exit()
    # 방향 안바꾸고 forwarding
    for i in range(1,4):
        nx,ny = forward(x,y,d,i)
        if 0<=nx<m and 0<=ny<n:
            if factory[nx][ny]==1:
                break
            elif visited[nx][ny][d]==0:
                visited[nx][ny][d] = t+1
                Q.append([nx,ny,d,t+1])
    # 방향 바꾸기
    for nd in turnDir(d):
        if visited[x][y][nd]==0:
            visited[x][y][nd] = t+1
            Q.append([x,y,nd,t+1])
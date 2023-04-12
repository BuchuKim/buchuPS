import sys;read=sys.stdin.readline
from collections import deque
k = int(read())
w,h = map(int,read().split())
graph = []
for _ in range(h):
    graph.append(list(map(int,read().split())))
cur = [0,0,0]
dx = [-1,1,0,0,2,2,-2,-2,1,1,-1,-1]
dy = [0,0,-1,1,1,-1,1,-1,2,-2,2,-2]
# visited[x][y][k] : k번 말로 이동했을 때 들렷냐?
visited = [[[sys.maxsize for _ in range(k+1)] for _ in range(w)] for _ in range(h)]
visited[0][0][0] = 0
def isValid(x,y):
    return 0<=x<h and 0<=y<w and graph[x][y]!=1
bfsQ = deque()
bfsQ.append(cur)
while bfsQ:
    x,y,cur_k = bfsQ.popleft()
    for i in range(12):
        if i>3 and cur_k+1>k:
            break
        nx = x + dx[i]
        ny = y + dy[i]
        if isValid(nx,ny):
            if i>3:
                if (visited[x][y][cur_k]+1<visited[nx][ny][cur_k+1]):
                    visited[nx][ny][cur_k+1] = visited[x][y][cur_k]+1
                    bfsQ.append([nx,ny,cur_k+1])
            else:
                if (visited[x][y][cur_k]+1<visited[nx][ny][cur_k]):
                    visited[nx][ny][cur_k] = visited[x][y][cur_k]+1
                    bfsQ.append([nx,ny,cur_k])
ans = min(visited[-1][-1])
if ans>w*h:
    print(-1)
else:
    print(ans)
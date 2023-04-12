import sys
from collections import deque
read = sys.stdin.readline
dx = [1,-1,0,0]
dy = [0,0,1,-1]
N,M = map(int,read().split())
graph = []
for i in range(N):
    graph.append(list(map(int,list(read().strip()))))
visited = [[[0,0] for _ in range(M)] for _ in range(N)]
# visited[n][m][0] : 벽 안부숨, visited[n][m][1]: 벽부숨
def search():
    bfsQ = deque()
    # 0,1: 좌표, 2: 거리
    bfsQ.append([0,0,0])
    visited[0][0][0] = 1
    while bfsQ:
        # d : 벽 부순 횟수
        a,b,d = bfsQ.popleft()
        if (a==N-1 and b==M-1):
            return visited[a][b][d]
        for i in range(4):
            x = a+dx[i]
            y = b+dy[i]
            if (0<=x<N and 0<=y<M):
                if (graph[x][y]==1 and d==0):
                    # 벽이 있고 아직 안부쉈어
                    visited[x][y][d+1] = visited[a][b][d] + 1
                    bfsQ.append([x,y,d+1])
                elif (graph[x][y]==0 and visited[x][y][d]==0):
                    visited[x][y][d] = visited[a][b][d] + 1
                    bfsQ.append([x,y,d])
    return -1
print(search())
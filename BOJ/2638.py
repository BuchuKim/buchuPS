import sys; read=sys.stdin.readline
from collections import deque
dx = [-1,1,0,0]
dy = [0,0,1,-1]
N,M = map(int,read().split())
graph = []
for i in range(N):
    li = list(map(int,read().split()))
    graph.append(li)

def search():
    visited = [[0 for _ in range(M)] for _ in range(N)]
    bfsQ = deque()
    bfsQ.append([0,0])
    visited[0][0] = 1
    while bfsQ:
        a,b = bfsQ.popleft()
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if (0<=x<N and 0<=y<M):
                if (graph[x][y]==1):
                    # cheeze
                    if (visited[x][y]==1):
                        graph[x][y] = 0
                    else:
                        visited[x][y] += 1
                else:
                    if (visited[x][y]==0):
                        visited[x][y] = 1
                        bfsQ.append([x,y])
def finished():
    for li in graph:
        if 1 in li:
            return False
    return True
answer = 0
while (not finished()):
    search()
    answer += 1
print(answer)
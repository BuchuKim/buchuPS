import sys;read=sys.stdin.readline
from collections import deque
N,M = map(int,read().split())
dx = [1,-1,0,0]
dy = [0,0,1,-1]
graph = []
output = [[0 for _ in range(M)] for _ in range(N)]
for i in range(N):
    li = list(map(int,list(read().rstrip())))
    graph.append(li)
visited = [[0 for _ in range(M)] for _ in range(N)]
def search(V,_id):
    # count 0
    ans = 1
    visited[V[0]][V[1]] = _id
    bfsQ = deque()
    bfsQ.append(V)
    while bfsQ:
        a,b = bfsQ.popleft()
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if (0<=x<N and 0<=y<M and graph[x][y]==0 and visited[x][y]==0):
                bfsQ.append([x,y])
                visited[x][y] = _id
                ans += 1
    return ans
zeros = {}
identifier = 1
for i in range(N):
    for j in range(M):
        if graph[i][j]==0 and visited[i][j]==0:
            zeros[identifier] = search([i,j],identifier)
            identifier += 1
for i in range(N):
    for j in range(M):
        if (graph[i][j]==1):
            ans = 1
            finished = []
            for k in range(4):
                x = i + dx[k]
                y = j + dy[k]
                if (0<=x<N and 0<=y<M and graph[x][y]==0):
                    if (visited[x][y] not in finished):
                        ans += zeros[visited[x][y]]
                        finished.append(visited[x][y])
            output[i][j] = (ans)%10
for li in output:
    for i in li:
        print(i,end='')
    print()
from sys import stdin
from collections import deque
m,n = map(int,stdin.readline().split())
graph = []
for _ in range(n):
    a = list(map(int,stdin.readline().split()))
    graph.append(a)
visited = [[0 for _ in range(m)] for _ in range(n)]
def done():
    for l in graph:
        if (0 in l):
            return False
    return True
def isValid(V):
    return 0<=V[0]<n and 0<=V[1]<m and visited[V[0]][V[1]]==0
def search(Vs):
    # 여러개 한 번에 bfs
    day = 0
    bfsQ = deque([])
    for V in Vs:
        V.append(0) # day
        visited[V[0]][V[1]] = 1
        bfsQ.append(V)
    while (bfsQ):
        V = bfsQ.popleft()
        if (isValid([V[0]-1,V[1]]) and graph[V[0]-1][V[1]]==0):
            visited[V[0]-1][V[1]] = 1
            graph[V[0]-1][V[1]] = 1
            bfsQ.append([V[0]-1,V[1],V[2]+1])
        if (isValid([V[0]+1,V[1]]) and graph[V[0]+1][V[1]]==0):
            visited[V[0]+1][V[1]] = 1
            graph[V[0]+1][V[1]] = 1
            bfsQ.append([V[0]+1,V[1],V[2]+1])
        if (isValid([V[0],V[1]-1]) and graph[V[0]][V[1]-1]==0):
            visited[V[0]][V[1]-1] = 1
            graph[V[0]][V[1]-1] = 1
            bfsQ.append([V[0],V[1]-1,V[2]+1])
        if (isValid([V[0],V[1]+1]) and graph[V[0]][V[1]+1]==0):
            visited[V[0]][V[1]+1] = 1
            graph[V[0]][V[1]+1] = 1
            bfsQ.append([V[0],V[1]+1,V[2]+1])
        day = V[2]+1
    if done():
        return day-1
    else:
        return -1

start = []
for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            start.append([i,j])
print(search(start))
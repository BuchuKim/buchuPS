import sys
from collections import deque
sys.setrecursionlimit(100000)
N,M = map(int,input().split())
graph = [[0 for _ in range(N+1)] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    graph[a][b] = graph[b][a] = 1
visited = [0 for _ in range(N+1)]
answer = 0
def search(V):
    global answer
    for i in range(1,N+1):
        if (graph[V][i]==1 and visited[i]==0):
            visited[i]=1
            search(i)
for i in range(1,N+1):
    if (visited[i]==0):
        answer += 1
        visited[i] = 1
        search(i)
print(answer)
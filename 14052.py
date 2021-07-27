import sys
from collections import deque
from itertools import permutations
n,m = map(int,sys.stdin.readline().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))
visited = [[0 for _ in range(m)] for _ in range(n)]
def isValid(V):
    return (0<=V[0]<n) and (0<=V[1]<m) and visited[V[0]][V[1]]==0
def search(V):
    # 안전 영역의 개수를 센다
    visited[V[0]][V[1]] = 1
    bfsQ = deque()
    while bfsQ:
        V = bfsQ.popleft()
        if (isValid([V[0]-1,V[1]]) and graph[V[0]-1][V[1]]==0):
            graph[V[0]-1][V[1]]=2
            visited[V[0]-1][V[1]] = 1
            bfsQ.append([V[0]-1][V[1]])
        if (isValid([V[0]+1,V[1]]) and graph[V[0]+1][V[1]]==0):
            graph[V[0]+1][V[1]]=2
            visited[V[0]+1][V[1]] = 1
            bfsQ.append([V[0]+1][V[1]])
        if (isValid([V[0],V[1]+1]) and graph[V[0]][V[1]]+1==0):
            graph[V[0]][V[1]+1]=2
            visited[V[0]][V[1]+1] = 1
            bfsQ.append([V[0]][V[1]+1])
        if (isValid([V[0],V[1]-1]) and graph[V[0]][V[1]]-1==0):
            graph[V[0]][V[1]-1]=2
            visited[V[0]][V[1]-1] = 1
            bfsQ.append([V[0]][V[1]-1])

# (0~n-1,0~m-1)에서 서로다른 3개 뽑기
a = permutations()

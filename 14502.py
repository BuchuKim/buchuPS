from sys import stdin
from collections import deque
from itertools import combinations
n,m = map(int,stdin.readline().split())
graph = []
zero = [] # 빈공간
virus = [] # 바이러스
dy = [1,-1,0,0]
dx = [0,0,1,-1]

for i in range(n):
    li = list(map(int,stdin.readline().split()))
    for j in range(m):
        if li[j]==0:
            zero.append([i,j])
        elif (li[j]==2):
            virus.append([i,j])
    graph.append(li)

def isValid(V,_visited):
    return (0<=V[0]<n) and (0<=V[1]<m) and _visited[V[0]][V[1]]==0
def search(V):
    bfsQ = deque(V)
    visited = [[0 for _ in range(m)] for _ in range(n)]
    while len(bfsQ)>0:
        V = bfsQ.popleft()
        for i in range(4):
            V2 = [V[0]+dy[i],V[1]+dx[i]]
            if (isValid(V2,visited) and graph[V2[0]][V2[1]]==0):
                graph[V2[0]][V2[1]] = 2
                visited[V2[0]][V2[1]] = 1
                bfsQ.append(V2)
    answer = 0
    for li in graph:
        for l in li:
            if l==0: answer += 1
    return answer

c = combinations(zero,3)
curmax = 0
for i in c:
    for j in i:
        graph[j[0]][j[1]] = 1
    curmax = max(curmax,search(virus))
    graph = [[1 for _ in range(m)] for _ in range(n)]
    for i in zero:
        graph[i[0]][i[1]] = 0
    for i in virus:
        graph[i[0]][i[1]] = 2

print(curmax)

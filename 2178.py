from sys import stdin
from collections import deque
N,M = map(int,stdin.readline().split())
graph = []
for _ in range(N):
    a = list(input())
    a = list(map(int,a))
    graph.append(a)
def isValid(V):
    return (0 <= V[0] < N and 0 <= V[1] < M)
def search(_graph):
    visited = [[0 for _ in range(M)] for _ in range(N)]
    bfsQ = deque([[[0,0],1]])
    while (len(bfsQ)>0):
        V = bfsQ.popleft() # V[0]: 좌표 [y,x], V[1]: step
        if (V[0][0]==N-1 and V[0][1]==M-1):
            return V[1]
        if (isValid(V[0]) and _graph[V[0][0]][V[0][1]]==1 and visited[V[0][0]][V[0][1]]==0):
            visited[V[0][0]][V[0][1]]=1
            bfsQ.append([[V[0][0]+1,V[0][1]],V[1]+1])
            bfsQ.append([[V[0][0]-1,V[0][1]],V[1]+1])
            bfsQ.append([[V[0][0],V[0][1]-1],V[1]+1])
            bfsQ.append([[V[0][0],V[0][1]+1],V[1]+1])
print(search(graph))
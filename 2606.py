from collections import deque
N = int(input())
K = int(input())
graph = [[0 for _ in range(N+1)] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
for _ in range(K):
    a,b = map(int,input().split())
    graph[a][b] = graph[b][a] = 1
answer = 0

def search(V):
    global answer
    bfsQ = deque()
    bfsQ.append(V)
    visited[V] = 1
    while len(bfsQ)>0:
        V = bfsQ.popleft()
        answer += 1
        for i in range(1,N+1):
            if (graph[V][i]==1 and visited[i]==0):
                visited[i] = 1
                bfsQ.append(i)

search(1)
print(answer-1)
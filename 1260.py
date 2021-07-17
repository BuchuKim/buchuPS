n,m,v = map(int,input().split())
# n : 정점 갯수, m : 간선 갯수, v : 시작하는 정점

visited1 = [0 for _ in range(n+1)] # dfs
visited2 = [0 for _ in range(n+1)] # bfs

# (n+1)*(n+1) 2중 리스트(index를 좀 더 직관적으로 보기 위해..)
# 연결되면 1, 연결되지 않으면 0
graph = [[0 for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1

def dfs(V):
    visited1[V] = 1
    print(V,end=' ')
    for i in range(1,n+1):
        if (graph[V][i]==1 and visited1[i]==0):
            dfs(i)

def bfs(V):
    visited2[V] = 1
    bfsQ = [V]
    for i in range(1,n+1):
        while (len(bfsQ)>0):
            V = bfsQ.pop(0)
            print(V,end=' ')
            for i in range(1,n+1):
                if (graph[V][i]==1 and visited2[i]==0):
                    bfsQ.append(i)
                    visited2[i] = 1

dfs(v)
print()
bfs(v)
print()






"""
graph = {}
for i in range(1,n+1):
    graph[i] = set()

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].add(b)
    graph[b].add(a)

for i in range(1,n+1):
    graph[i] = list(set(graph[i]))
print(graph)
visited = [0 for _ in range(n+1)]
def dfs(V):
    visited[V] = 1
    print(V,end=' ')
    for i in range(len(graph[V])):
        if (visited[graph[V][i]]==0):
            dfs(graph[V][i])
def bfs(V):
    visited[V] = 1
    bfsQ = [V]
    while (len(bfsQ)>0):
        V = bfsQ.pop(0)
        print(V,end=' ')
        for i in range(len(graph[V])):
            if (visited[graph[V][i]]==0):
                bfsQ.append(graph[V][i])
                visited[graph[V][i]]=1
dfs(v)
print()
visited = [0 for _ in range(n+1)]
bfs(v)
print()
"""
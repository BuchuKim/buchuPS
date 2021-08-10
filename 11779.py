from sys import stdin; read = stdin.readline

n = int(read()) # 도시
m = int(read()) # 버스
graph = [[100000 for _ in range(n+1)] for _ in range(n+1)]
for i in range(1,m+1):
    s,e,c = map(int,read().split())
    graph[s][e] = c
start, end = map(int,read().split())

# 다익스트라 알고리즘
visited = [0 for _ in range(n+1)]
def short(V): # 가장 작은 거리 + 아직 들리지 않은 노드 return
    minc = 100000
    minv = 0
    for i in range(n+1):
        if (visited[i]==0 and graph[V][i]<minc):
            minc = graph[V][i]
            minv = i
    return minv
def search(V):
    # V : 시작
    path = [['' for _ in range(n+1)] for _ in range(n+1)]
    dis = [100000 for _ in range(n+1)]
    for i in range(1,n+1):
        dis[i] = graph[V][i]
    visited[V] = 1
    for i in range(n-1):
        shortv = short(V)
        if (shortv==0): break
        visited[shortv] = 1
        for j in range(1,n+1):
            if (visited[j]==0):
                if (dis[j] > dis[shortv]+graph[shortv][j]): # shortv를 거쳐가야한다는 것!
                    path[V][j] = path[V][shortv] + str(shortv) + path[shortv][j]
                    dis[j] = dis[shortv]+graph[shortv][j]
    return dis[end], path[start][end]

answer, p = search(start)
print(answer)
print(len(p)+2)
print(start,end=' ')
for s in p:
    print(s,end=' ')
print(end)
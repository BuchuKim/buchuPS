import sys
from heapq import heappush,heappop
read = sys.stdin.readline
TC = int(read())
inf = sys.maxsize
def search(g,d):
    # return Fase if no loop, True if loop
    d[1] = 0
    for i in range(1,len(d)):
        for j in range(1,len(d)):
            for node,cost in g[j]:
                if (dis[node]>dis[j]+cost):
                    dis[node] = dis[j] + cost
                    if (i==N):
                        return True
    return False

for _ in range(TC):
    N,M,W = map(int,read().split())
    graph = [[] for _ in range(N+1)]
    dis = [inf] * (N+1)
    for _ in range(M):
        S,E,T = map(int,read().split())
        graph[S].append([E,T])
        graph[E].append([S,T])
    for _ in range(W):
        S,E,T = map(int,read().split())
        graph[S].append([E,-T])
    if (search(graph,dis)):
        print("YES")
    else:
        print("NO")
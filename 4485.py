import sys;read=sys.stdin.readline
from heapq import heappop,heappush
n = int(input())
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def isValid(a,b):
    return 0<=a<n and 0<=b<n
p = 1
while (n!=0):
    graph = []
    for _ in range(n):
        graph.append(list(map(int,read().split())))
    dis = [[sys.maxsize for _ in range(n)] for _ in range(n)] # 최단거리 for graph[x][y]
    dis[0][0] = graph[0][0]
    heap = []
    heappush(heap,[graph[0][0],0,0])
    while heap:
        cost,x,y = heappop(heap)
        if cost>dis[x][y]:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if isValid(nx,ny) and dis[nx][ny]>cost+graph[nx][ny]:
                dis[nx][ny] = cost+graph[nx][ny]
                heappush(heap,[dis[nx][ny],nx,ny])
    print("Problem ",p,": ",dis[n-1][n-1],sep="")
    p += 1
    n = int(input())
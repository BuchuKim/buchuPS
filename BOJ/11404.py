import sys;read=sys.stdin.readline
inf = sys.maxsize
n = int(read())
m = int(read())
graph = [[inf for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,read().split())
    if (graph[a][b] > c):
        graph[a][b] = c
def search():# 플로이드 - 워셜
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if (i!=j and graph[i][j]>graph[i][k]+graph[k][j]):
                    graph[i][j] = graph[i][k]+graph[k][j]
search()
for i in range(1,n+1):
    for j in range(1,n+1):
        if (graph[i][j]<inf):
            print(graph[i][j],end=' ')
        else:
            print(0,end=' ')
    print()
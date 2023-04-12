import sys;input=sys.stdin.readline
n = int(input())
graph = []
need = [[True for _ in range(n)] for _ in range(n)]
ans = 0
for i in range(n):
    graph.append(list(map(int,input().split())))
for k in range(n):
    for i in range(n):
        for j in range(n):
            if k==i or i==j or k==j:
                continue
            if graph[i][j]==graph[i][k]+graph[k][j]:
                # 필요없는놈
                need[i][j] = False
            elif graph[i][j]>graph[i][k]+graph[k][j]:
                print(-1)
                exit()
for i in range(n-1):
    for j in range(i+1,n):
        if need[i][j]:
            ans += graph[i][j]
print(ans)
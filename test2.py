N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int,input().split())))

for i in range(3):
    for j in range(3):
        g = graph[i*(N//3):(i+1)*(N//3)]
        for k in range(N//3):
            g[k] = g[k][j*(N//3):(j+1)*(N//3)]
        print(g)
        print()
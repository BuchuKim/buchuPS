# 11403 경로찾기
N = int(input())

# 그래프 받기
graph = []
for _ in range(N):
    graph.append(list(map(int,input().split())))

def FW(_graph):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if (_graph[i][k]==1 and _graph[k][j]==1):
                    _graph[i][j]=1

FW(graph)
for a in graph:
    for b in a:
        print(b,end=' ')
    print()
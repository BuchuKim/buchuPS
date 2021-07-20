import sys
sys.setrecursionlimit(10000)
N = int(input())
graph = []
for _ in range(N):
    graph.append(list(input()))

visited = [[0 for _ in range(N)] for _ in range(N)]
def isValid(V):
    # 범위가 맞는지, 들린 노드가 아닌지 확인
    return (0<=V[0]<N and 0<=V[1]<N and visited[V[0]][V[1]]==0)
def search(_graph,V,_color):
    visited[V[0]][V[1]] = 1
    if (isValid([V[0]-1,V[1]]) and _color==_graph[V[0]-1][V[1]]):
        # 범위에 맞고, 아직 들리지 않았고, 색마저 같다면 같은 영역에 포함되어 있는 것임
        search(_graph,[V[0]-1,V[1]],_color)
    if (isValid([V[0]+1,V[1]]) and _color==_graph[V[0]+1][V[1]]):
        search(_graph,[V[0]+1,V[1]],_color)
    if (isValid([V[0],V[1]-1]) and _color==_graph[V[0]][V[1]-1]):
        search(_graph,[V[0],V[1]-1],_color)
    if (isValid([V[0],V[1]+1]) and _color==_graph[V[0]][V[1]+1]):
        search(_graph,[V[0],V[1]+1],_color)

visited2 = [[0 for _ in range(N)] for _ in range(N)]
def isValid2(V):
    return (0<=V[0]<N and 0<=V[1]<N and visited2[V[0]][V[1]]==0)
def search2(_graph,V,_color):
    # 적록색약
    visited2[V[0]][V[1]] = 1
    if  (_color in "RG"):
        if (isValid2([V[0]-1,V[1]]) and _graph[V[0]-1][V[1]] in "RG"):
            search2(_graph,[V[0]-1,V[1]],_color)
        if (isValid2([V[0]+1,V[1]]) and _graph[V[0]+1][V[1]] in "RG"):
            search2(_graph,[V[0]+1,V[1]],_color)
        if (isValid2([V[0],V[1]-1]) and _graph[V[0]][V[1]-1] in "RG"):
            search2(_graph,[V[0],V[1]-1],_color)
        if (isValid2([V[0],V[1]+1]) and _graph[V[0]][V[1]+1] in "RG"):
            search2(_graph,[V[0],V[1]+1],_color)
    else:
        if (isValid2([V[0]-1,V[1]]) and _graph[V[0]-1][V[1]]==_color):
            search2(_graph,[V[0]-1,V[1]],_color)
        if (isValid2([V[0]+1,V[1]]) and _graph[V[0]+1][V[1]]==_color):
            search2(_graph,[V[0]+1,V[1]],_color)
        if (isValid2([V[0],V[1]-1]) and _graph[V[0]][V[1]-1]==_color):
            search2(_graph,[V[0],V[1]-1],_color)
        if (isValid2([V[0],V[1]+1]) and _graph[V[0]][V[1]+1]==_color):
            search2(_graph,[V[0],V[1]+1],_color)

answer = 0
answer2 = 0
for i in range(N):
    for j in range(N):
        if (visited[i][j]==0):
            answer += 1
            search(graph,[i,j],graph[i][j])
        if (visited2[i][j]==0):
            answer2 += 1
            search2(graph,[i,j],graph[i][j])
print(answer,answer2)
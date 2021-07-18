N = int(input())
answer = 0
arr = []
cnum = 0

graph=[[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    a = input()
    for j in range(N):
        graph[i][j] = int(a[j])

visited = [[0 for _ in range(N)] for _ in range(N)]
def isValid(V):
    return (0<=V[0]<N and 0<=V[1]<N and visited[V[0]][V[1]]==0)
def dfs(_graph,V):
    global cnum
    cnum += 1
    visited[V[0]][V[1]] = 1
    if (isValid([V[0]-1,V[1]]) and _graph[V[0]-1][V[1]]==1):
        dfs(_graph,[V[0]-1,V[1]])
    if (isValid([V[0]+1,V[1]]) and _graph[V[0]+1][V[1]]==1):
        dfs(_graph,[V[0]+1,V[1]])
    if (isValid([V[0],V[1]+1]) and _graph[V[0]][V[1]+1]==1):
        dfs(_graph,[V[0],V[1]+1])
    if (isValid([V[0],V[1]-1]) and _graph[V[0]][V[1]-1]==1):
        dfs(_graph,[V[0],V[1]-1])

for i in range(N):
    for j in range(N):
        if (visited[i][j]==0 and graph[i][j]==1):
            cnum = 0
            answer += 1
            dfs(graph,[i,j])
            arr.append(cnum)
arr.sort()
print(answer)
for i in arr:
    print(i)
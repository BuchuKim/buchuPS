import sys; read=sys.stdin.readline
r,c,t = map(int,read().split())
graph = []
cheong = []
dx = [1,-1,0,0]
dy = [0,0,-1,1]
for i in range(r):
    li = list(map(int,read().split()))
    graph.append(li)
    if li[0]==-1:
        cheong.append(i)
def hwak():
    newgraph = [[0] * (c) for _ in range(r)]
    newgraph[cheong[0]][0] = -1
    newgraph[cheong[1]][0] = -1
    for i in range(r):
        for j in range(c):
            if (graph[i][j]>0):
                mise = graph[i][j]//5
                banghyang = 0
                for k in range(4):
                    x = i + dx[k]
                    y = j + dy[k]
                    if (0<=x<r and 0<=y<c and graph[x][y]!=-1):
                        newgraph[x][y] += mise
                        banghyang += 1
                newgraph[i][j] += graph[i][j] - (mise * banghyang)
    return newgraph
def gongcheong():
    a,b = cheong[0],cheong[1]
    # a가 위, b가 아래
    for i in range(b+1,r-1):
        graph[i][0] = graph[i+1][0]
    i = a-1
    while (i>=1):
        graph[i][0] = graph[i-1][0]
        i -= 1
    for i in range(c-1):
        graph[-1][i] = graph[-1][i+1]
        graph[0][i] = graph[0][i+1]
    i = r-1
    while (i>=b+1):
        graph[i][-1] = graph[i-1][-1]
        i -= 1
    for i in range(a):
        graph[i][-1] = graph[i+1][-1]
    i = c-1
    while (i>=2):
        graph[b][i] = graph[b][i-1]
        graph[a][i] = graph[a][i-1]
        i-=1
    graph[b][1] = 0
    graph[a][1] = 0
def mise():
    ans = 0
    for li in graph:
        ans += sum(li)
    return ans + 2

for _ in range(t):
    graph = hwak()
    gongcheong()
print(mise())
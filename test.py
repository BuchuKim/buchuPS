import sys;read=sys.stdin.readline
sys.setrecursionlimit(10000000)
m,n = map(int,read().split())
graph = []
for _ in range(m):
    graph.append(list(map(int,read().split())))
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def isValid(x,y):
    return 0<=x<m and 0<=y<n
def search(x,y,visited):
    visited[x][y] += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (isValid(nx,ny) and visited[nx][ny]!=-1 and graph[nx][ny]<graph[x][y]):
            search(nx,ny,visited)
# visited[i]][j] : 0,0에서 i,j까지 올 수 있는 경우의 수..
visited = [[-1 for _ in range(n)] for _ in range(m)]
search(0,0,visited)
print(visited[-1][-1]+1)
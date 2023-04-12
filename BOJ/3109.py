import sys;input=sys.stdin.readline
r,c = map(int,input().split())
graph = []
for _ in range(r):
    graph.append(list(input().rstrip()))
visited = [[0 for _ in range(c)] for _ in range(r)]
dx = [-1,0,1]
ans = 0
def search(x,y):
    global connected, ans
    visited[x][y] = 1
    if y==c-1:
        connected = True
        ans += 1
        return
    for i in range(3):
        nx,ny = x+dx[i],y+1
        if 0<=nx<r and 0<=ny<c and graph[nx][ny]!='x' and visited[nx][ny]==0:
            if not connected:
                search(nx,ny)
for i in range(r):
    connected = False
    search(i,0)
print(ans)
import sys;read=sys.stdin.readline
n = int(read())
forest = []
for _ in range(n):
    forest.append(list(map(int,read().split())))
dx = [-1,1,0,0]
dy = [0,0,-1,1]
ans = 0
dp = [[0 for _ in range(n)] for _ in range(n)]
# (x,y)에서 시작했을 때 가장 멀리 갈 수 있는 수
def search(x,y):
    global ans
    if dp[x][y]!=0:
        # searched
        return dp[x][y]
    dp[x][y] = 1
    for i in range(4):
        nx, ny = x+dx[i],y+dy[i]
        if 0<=nx<n and 0<=ny<n and forest[x][y]<forest[nx][ny]:
            dp[x][y] = max(search(nx,ny)+1,dp[x][y])
    ans = max(dp[x][y],ans)
    return dp[x][y]
for i in range(n):
    for j in range(n):
        search(i,j)
print(ans)
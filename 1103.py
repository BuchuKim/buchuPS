import sys;read=sys.stdin.readline
sys.setrecursionlimit(100000)
n,m = map(int,read().split())
board = []
for _ in range(n):
    li = list(read().rstrip())
    for i in range(m):
        if (li[i]!="H"):
            li[i] = int(li[i])
    board.append(li)
dx = [-1,1,0,0]
dy = [0,0,-1,1]
ans = 0
dp = [[0 for _ in range(m)] for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
def search(x,y,count):
    global ans
    ans = max(count,ans)
    num = board[x][y]
    for i in range(4):
        nx = x + num * dx[i]
        ny = y + num * dy[i]
        if (0<=nx<n and 0<=ny<m and board[nx][ny]!="H" and dp[nx][ny]<count+1):
            if visited[nx][ny]!=0:
                print(-1)
                exit()
            dp[nx][ny] = count + 1
            visited[nx][ny] = 1
            search(nx,ny,count+1)
            visited[nx][ny] = 0
search(0,0,0)
print(ans+1)
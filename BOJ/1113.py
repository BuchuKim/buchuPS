import sys;input=sys.stdin.readline
from collections import deque
n,m = map(int,input().split())
pool = [list(map(int,list(input().rstrip()))) for _ in range(n)]
dx,dy = [1,-1,0,0],[0,0,-1,1]

def search(a,b,z):
    # z층에서 현재 물이 차오를 수 있는 영역 
    water = 1
    visit,fail = [],False
    Q = deque([[a,b]])
    while Q:
        x,y = Q.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if (nx<0 or nx>=n) or (ny<0 or ny>=m):
                fail = True
            elif not visited[nx][ny] and pool[nx][ny]<z:
                visited[nx][ny] = True
                visit.append([nx,ny])
                if no[nx][ny]:
                    fail = True
                else:
                    water += 1
                Q.append([nx,ny])
    if fail:
        for x,y in visit:
            no[x][y] = True
        return 0
    return water

ans = 0
for k in range(2,10):
    # k : 물의 높이
    visited = [[False for _ in range(m)] for _ in range(n)]
    no = [[False for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if k>pool[i][j] and not visited[i][j]:
                visited[i][j] = True
                ans += search(i,j,k)
print(ans)
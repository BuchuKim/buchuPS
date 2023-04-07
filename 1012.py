import sys; input=sys.stdin.readline
from collections import deque

def isValid(m,n,x,y):
    return 0<=x<m and 0<=y<n

def search(field,m,n):
    ans = 0
    dx,dy = [0,0,-1,1],[-1,1,0,0]
    visited = [[False for _ in range(m)] for _ in range(n)]
    for y in range(n):
        for x in range(m):
            if (field[y][x]==1 and not visited[y][x]):
                visited[y][x] = True
                ans += 1
                Q = deque()
                Q.append((x,y))
                while Q:
                    qx,qy = Q.popleft()
                    for i in range(4):
                        nx,ny = qx+dx[i],qy+dy[i]
                        if ((isValid(m,n,nx,ny)) and (field[ny][nx]==1) and (not visited[ny][nx])):
                            visited[ny][nx] = True
                            Q.append((nx,ny))
    return ans

for _ in range(int(input())):
    m,n,k = map(int,input().split())
    field = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        x, y = map(int,input().split())
        field[y][x] = 1
    print(search(field,m,n))

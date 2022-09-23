import sys;input=sys.stdin.readline
from collections import deque

r,c = map(int,input().split())
tw,gosum,bieber,water = [],[],[],[]
g_visited,w_visited = [[False for _ in range(c)] for _ in range(r)],[[False for _ in range(c)] for _ in range(r)]
for i in range(r):
    li = list(input().rstrip())
    tw.append(li)
    for j in range(c):
        if li[j]=="D":
            bieber = [i,j]
        elif li[j]=="S":
            gosum = [i,j]
            g_visited[i][j]=True
        elif li[j]=="*":
            w_visited[i][j] = True
            water.append([i,j,0,True])

def isValid(x,y):
    return 0<=x and x<r and 0<=y and y<c and tw[x][y]!="X"
dx,dy = [1,-1,0,0],[0,0,1,-1]
Q = deque(water+[gosum+[0,False]])
while Q:
    x,y,t,isWater = Q.popleft()
    if isWater:
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if isValid(nx,ny) and not w_visited[nx][ny] and tw[nx][ny]!="D":
                tw[nx][ny] = "*"
                w_visited[nx][ny] = True
                Q.append([nx,ny,t+1,True])
    else:
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if not isValid(nx,ny):
                continue
            if tw[nx][ny]=="D":
                print(t+1)
                exit()
            if not g_visited[nx][ny] and tw[nx][ny]==".":
                g_visited[nx][ny] = True
                Q.append([nx,ny,t+1,False])
    
print("KAKTUS")
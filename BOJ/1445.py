import sys; read=sys.stdin.readline
from heapq import heappop,heappush
n,m = map(int,read().split())
graph = []
start = [0,0]
end = [0,0]
for i in range(n):
    li = list(read().rstrip())
    graph.append(li)
    for j in range(m):
        if li[j]=="S":
            start = [i,j]
        elif li[j]=="F":
            end = [i,j]
def isValid(x,y):
    return 0<=x<n and 0<=y<m
Q = [[0,0,start[0],start[1]]]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
# [쓰레기 지난 횟수, 쓰레기 옆 지난 횟수]
dis = [[[n*m,n*m] for _ in range(m)] for _ in range(n)]
dis[start[0]][start[1]] = [0,0]
while Q:
    g_num, n_num, x, y = heappop(Q)
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if isValid(nx,ny) and (nx!=end[0] or ny!=end[1]):
            n_g_num, n_n_num = g_num, n_num
            if graph[nx][ny]=="g":
                n_g_num +=1
            else:
                for j in range(4):
                    if isValid(nx+dx[j],ny+dy[j]) and graph[nx+dx[j]][ny+dy[j]]=="g":
                        n_n_num +=1
                        break
            if dis[nx][ny][0]>n_g_num:
                dis[nx][ny] = [n_g_num,n_n_num]
                heappush(Q,[n_g_num,n_n_num,nx,ny])
            elif dis[nx][ny][0]==n_g_num and dis[nx][ny][1]>n_n_num:
                dis[nx][ny] = [n_g_num,n_n_num]
                heappush(Q,[n_g_num,n_n_num,nx,ny])
        elif nx==end[0] and ny==end[1]:
            if dis[nx][ny][0]>g_num:
                dis[nx][ny] = [g_num,n_num]
            elif dis[nx][ny][0]==g_num and dis[nx][ny][1]>n_num:
                dis[nx][ny] = [g_num,n_num]
print(dis[end[0]][end[1]][0],dis[end[0]][end[1]][1])
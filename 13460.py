# 중력을 이용해 빨간구슬을 구멍 바깥으로 빼되, 파란 구슬이 나오면 안됨
# 동시에 빠져도 실패 (동시에 같은 공간에 있을 수 없음)
# 10번 이하로 움직여서 빨간구슬 뺄 수 없으면 -1
import sys;read=sys.stdin.readline
from copy import deepcopy
from collections import deque
N,M = map(int,read().split())
graph=[]
red = [0,0]
blue = [0,0]
hole = [0,0]
for i in range(N):
    li = list(read().rstrip())
    if ('B' in li):
        blue[0] = i
        blue[1] = li.index('B')
    if ('R' in li):
        red[0] = i
        red[1] = li.index('R')
    if ('O' in li):
        hole[0] = i
        hole[1] = li.index('O')
    graph.append(li)

dx = [1,-1,0,0]
dy = [0,0,1,-1]
def search():
    global graph
    ograph = deepcopy(graph)
    bfsQ = deque()
    bfsQ.append([red[0],red[1],blue[0],blue[1],0])
    while bfsQ:
        rx,ry,bx,by,a = bfsQ.popleft()
        for i in range(4):
            modified = False
            possible = True
            finished = False
            nrx,nry,nbx,nby = rx,ry,bx,by
            graph = deepcopy(ograph)
            graph[red[0]][red[1]] = '.'
            graph[blue[0]][blue[1]] = '.'
            graph[rx][ry] = 'R'
            graph[bx][by] = 'B'
            while ((graph[nrx+dx[i]][nry+dy[i]] in '.O' and not finished) or (graph[nbx+dx[i]][nby+dy[i]] in '.O')):
                modified = True
                if (graph[nrx+dx[i]][nry+dy[i]] in '.O' and not finished):
                    graph[nrx][nry] = '.'
                    nrx += dx[i]
                    nry += dy[i]
                    if (graph[nrx][nry]=='O'):
                        finished = True
                    if not finished:
                        graph[nrx][nry] = 'R'
                if (graph[nbx+dx[i]][nby+dy[i]] in '.O'):
                    graph[nbx][nby] = '.'
                    nbx += dx[i]
                    nby += dy[i]
                    if (graph[nbx][nby]=='O'):
                        possible = False
                        break
                    graph[nbx][nby] = 'B'
            if (finished):
                if possible:
                    return a+1
            if (modified and possible):
                if (a+1<10):
                    bfsQ.append([nrx,nry,nbx,nby,a+1])
    return -1
print(search())
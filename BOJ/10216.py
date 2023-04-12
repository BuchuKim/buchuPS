import sys;input=sys.stdin.readline
from collections import deque
import math
def dis(x1,y1,x2,y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)
def search(x,y,r):
    for ni,nx,ny,nr in tower:
        if (not visited[ni]) and dis(x,y,nx,ny)<=r+nr:
            visited[ni] = True
            search(nx,ny,nr)
for _ in range(int(input())):
    n = int(input())
    tower = deque()
    visited = [False for i in range(n)]
    ans = 0
    for i in range(n):
        tower.append([i]+list(map(int,input().split())))
    while tower:
        i,x,y,r = tower.popleft()
        if not visited[i]:
            visited[i] = True
            ans += 1
            search(x,y,r)
    print(ans)
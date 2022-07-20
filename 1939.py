import sys;input=sys.stdin.readline
from collections import deque
n,m = map(int,input().split())
land = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    land[a].append([b,c])
    land[b].append([a,c])

a,b = map(int,input().split())
def search(cost):
    visited = [0 for _ in range(n+1)]
    Q = deque()
    visited[a] = 1
    Q.append(a)
    while Q:
        node = Q.popleft()
        if node==b:
            return True
        for nei,limit in land[node]:
            if visited[nei]==0 and limit>=cost:
                visited[nei] = 1
                Q.append(nei)
    return False
s,e,ans = 0, 1000000000, 0
while s<=e:
    mid = (s+e)//2
    if search(mid):
        ans = mid
        s = mid+1
    else:
        e = mid-1
print(ans)
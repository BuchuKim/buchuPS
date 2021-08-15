import sys
from collections import deque
read = sys.stdin.readline
N = int(read())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b,c = map(int,read().split())
    tree[a].append([b,c])
    tree[b].append([a,c])
def search(V):
    visited = [0 for _ in range(N+1)]
    bfsQ = deque()
    bfsQ.append([V,0])
    visited[V] = 1
    farnode = 0
    jirum = 0
    while bfsQ:
        V,C = bfsQ.popleft()
        if (C>jirum):
            farnode = V
            jirum = C
        for node,cost in tree[V]:
            if (visited[node]==0):
                bfsQ.append([node,C+cost])
                visited[node] = 1
    return farnode,jirum
far,_ = search(1)
_,answer = search(far)
print(answer)
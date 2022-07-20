import sys;read=sys.stdin.readline
n,m = map(int,read().split())
parent = [i for i in range(n+1)]
def find(x):
    while x!=parent[x]:
        x = parent[x]
    parent[x] = x
    return x
def union(x,y):
    x = find(x)
    y = find(y)
    if x<y:
        parent[y] = x
    elif y<x:
        parent[x] = y
for _ in range(m):
    op,a,b = map(int,read().split())
    if op==0:
        union(a,b)
    else:
        if find(a)==find(b):
            print('YES')
        else:
            print('NO')

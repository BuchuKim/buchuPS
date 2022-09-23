import sys;input=sys.stdin.readline
n = int(input())
m = int(input())
parent = [i for i in range(n+1)]
def find(x):
    p = parent[x]
    while parent[p]!=p:
        p = parent[p]
    parent[x] = p
    return p
def union(x,y):
    x,y = find(x),find(y)
    if x>y:
        parent[x] = y
    elif y>x:
        parent[y] = x
edges = []
for _ in range(m):
    a,b,c = map(int,input().split())
    edges.append([c,a,b])
edges.sort()
ans = 0
for c,a,b in edges:
    if find(a)!=find(b):
        union(a,b)
        ans += c
print(ans)

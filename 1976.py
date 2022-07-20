import sys;input=sys.stdin.readline
n = int(input())
m = int(input())
parent = [i for i in range(n+1)]
def find(x):
    p = parent[x]
    while p!=parent[p]:
        p = parent[p]
    parent[x] = p
    return p
def union(x,y):
    x = find(x)
    y = find(y)
    if x<y:
        parent[y] = x
    else:
        parent[x] = y
for i in range(1,n+1):
    li = [0]+list(map(int,input().split()))
    for j in range(1,n+1):
        if li[j]==1:
            union(i,j)
trip = list(map(int,input().split()))
p = find(trip[0])
for c in trip:
    if find(c)!=p:
        print('NO')
        exit()
print('YES')
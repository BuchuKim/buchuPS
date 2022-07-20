import sys;input=sys.stdin.readline
sys.setrecursionlimit(10**9)
n,m = map(int,input().split())
parent = [0] + list(map(int,input().split()))
got = [0 for _ in range(n+1)]
for _ in range(m):
    i,w = map(int,input().split())
    got[i] += w
children = {1:[]}
for i in range(2,n+1):
    if i not in children:
        children[i] = []
    children[parent[i]].append(i)
def search(v):
    for child in children[v]:
        got[child] += got[v]
        search(child)
search(1)
for i in range(1,n+1):
    print(got[i],end=' ')
print()
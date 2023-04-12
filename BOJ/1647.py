import sys;read=sys.stdin.readline
N,M = map(int,read().split())
graph = []
for _ in range(M):
    a,b,c = map(int,read().split())
    graph.append([c,a,b])
graph.sort()
arr = [i for i in range(N+1)] # for union-find
def union(x,y):
    x = find(x)
    y = find(y)
    if (x==y):
        return False
    else:
        if (x>y):
            arr[x] = y
        else:
            arr[y] = x
        return True
def find(x):
    while (arr[x]!=x):
        x = arr[x]
    return x
cost = []
ans = 0
for c,a,b in graph:
    if (union(a,b)):
        cost.append(c)
        ans += c
print(ans-cost[-1])
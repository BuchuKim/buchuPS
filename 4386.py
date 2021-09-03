import sys;read=sys.stdin.readline
import math
import itertools
itertools.permutations()
N = int(read())
stars = []
cost = []
for _ in range(N):
    stars.append(list(map(float,read().split())))
for i in range(N-1):
    for j in range(i+1,N):
        cost.append([math.dist(stars[i],stars[j]),i,j])
cost.sort()
arr = [i for i in range(N)]
def find(x):
    while (x!=arr[x]):
        x = arr[x]
    return x
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
ans = 0
for c,a,b in cost:
    if (union(a,b)):
        ans += c
print(ans)
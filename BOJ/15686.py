import sys
from itertools import combinations
read = sys.stdin.readline
N,M = map(int,read().split())
home = []
chicken = []
for i in range(N):
    a = list(map(int,read().split()))
    for j in range(N):
        if a[j]==1:
            home.append([i,j])
        elif a[j]==2:
            chicken.append([i,j])
chicken = list(combinations(chicken,M))

ans = N*N*len(home)
for i in range(len(chicken)):
    dis = [N*N] * len(home)
    for c in chicken[i]:
        for j in range(len(home)):
            dis[j] = min(dis[j],abs(c[0]-home[j][0])+abs(c[1]-home[j][1]))
    ans = min(ans,sum(dis))
print(ans)
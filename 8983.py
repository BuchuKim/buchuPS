import sys;input=sys.stdin.readline
from bisect import bisect_left

def dis(s,x,y):
    return abs(x-s)+y

m,n,l = map(int,input().split())
ans = 0
shot = list(map(int,input().split()))
shot.sort()
animal = [list(map(int,input().split())) for _ in range(n)]
for x,y in animal:
    i = bisect_left(shot,x)
    if i==m:
        i -= 1
    if dis(shot[i],x,y)<=l or dis(shot[i-1],x,y)<=l:
        ans += 1
print(ans)
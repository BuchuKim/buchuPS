import sys;input=sys.stdin.readline
from bisect import bisect_left
n = int(input())
yong = list(map(int,input().split()))
yong.sort()
zero = bisect_left(yong,0)
if n==2 or zero==0:
    print(yong[0],yong[1])
    exit()
elif zero>=n:
    print(yong[-2],yong[-1])
l,ans,cur = 0,[0,n-1],1000000000
while l<=zero:
    r = bisect_left(yong,-yong[l])
    if r==n:
        r -= 1
    if abs(yong[l]+yong[r])<ans:
        ans = abs(yong[l]+yong[r])
        ans = [l,r]
    if r-1>=zero and abs(yong[l]+yong[r])<ans:
        ans = abs(yong[l]+yong[r-1])
        ans = [l,r-1]
    l += 1
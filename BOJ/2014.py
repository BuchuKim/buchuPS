import sys;input=sys.stdin.readline
from heapq import heappop,heappush
K,N = map(int,input().split())
sosu = list(map(int,input().split()))
li=[]
for i in sosu:
    heappush(li,i)
for i in range(N):
    n = heappop(li)
    for j in sosu:
        heappush(li,n*j)
        if n%j==0:
            break
print(n)
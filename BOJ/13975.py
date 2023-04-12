import sys;input=sys.stdin.readline
from heapq import heappush,heappop,heapify
for _ in range(int(input())):
    k = int(input())
    ans = 0
    file = list(map(int,input().split()))
    heapify(file)
    while True:
        a = heappop(file)
        if not file:
            break
        hap = a+heappop(file)
        ans += hap
        heappush(file,hap)
    print(ans)
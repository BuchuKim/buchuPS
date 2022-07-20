# 가장 데드라인이 빨리 있는 놈을..
import sys;input=sys.stdin.readline
from heapq import heappop,heappush
for _ in range(int(input())):
    n,m = map(int,input().split())
    heap = [[] for _ in range(n+1)]
    for i in range(m):
        a,b = map(int,input().split())
        for j in range(a,b+1):
            heappush(heap[j],[b,i])
    ans = 0
    received = [False for _ in range(m)]
    for i in range(1,n+1):
        while heap[i]:
            ran,student = heappop(heap[i])
            if not received[student]:
                received[student] = True
                ans += 1
                break
    print(ans)
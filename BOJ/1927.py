from sys import stdin
import heapq
N = int(stdin.readline())
Q = []
for _ in range(N):
    c = int(stdin.readline())
    if c==0:
        if Q:
            print(heapq.heappop(Q))
        else:
            print(0)
    else:
        heapq.heappush(Q,c)
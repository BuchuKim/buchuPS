import sys; read=sys.stdin.readline
from heapq import heapify,heappop

N = int(read())
overlap = 0
ans = 1

time = []
for i in range(N):
    s,e = map(int,read().split())
    time.append([s,1])
    time.append([e,-1])
heapify(time)

while time:
    t, flag = heappop(time)
    overlap += flag
    ans = max(overlap,ans)

print(ans)
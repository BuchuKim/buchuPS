import sys;read=sys.stdin.readline
from heapq import heappop,heapify,heappush
N = int(read())
cl = []
need = 0
ans = 0
# alloc[i] : i번 수업에 할당된 강의실
alloc = [0 for _ in range(N+1)]
for _ in range(N):
    n,s,e = map(int,read().split())
    cl.append([s,1,n])
    cl.append([e,-1,n])
heapify(cl)
room = [i for i in range(1,N+1)]
heapify(room)
while cl:
    time, isStart, n = heappop(cl)
    need += isStart
    ans = max(ans,need)
    if isStart==1:
        alloc[n] = heappop(room)
    else:
        heappush(room,alloc[n])
print(ans)
for i in range(1,N+1):
    print(alloc[i])
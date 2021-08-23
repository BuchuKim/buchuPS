import sys; read=sys.stdin.readline
from heapq import heappush,heappop
N,K = map(int,read().split())
def search():
    visited = [-1 for _ in range(100001)]
    heap = []
    heappush(heap,[0,N])
    visited[N] = 0
    while heap:
        time,cur = heappop(heap)
        if (cur*2<=100000 and (visited[cur*2]<0 or visited[cur*2]>time)):
            heappush(heap,[time,2*cur])
            visited[cur*2] = time
        if (cur<K and (visited[cur+1]<0 or visited[cur+1]>time+1)):
            heappush(heap,[time+1,cur+1])
            visited[cur+1] = time + 1
        if (cur>=1 and (visited[cur-1]<0 or visited[cur-1]>time+1)):
            heappush(heap,[time+1,cur-1])
            visited[cur-1] = time + 1
    return visited[K]
print(search())
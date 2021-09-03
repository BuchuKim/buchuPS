import sys;read=sys.stdin.readline
from heapq import heappop,heappush
bosuk = []
bag = []
ans = 0
N,K = map(int,read().split())
for _ in range(N):
    # [M,V]
    m,v = map(int,read().split())
    bosuk.append([m,v])
for _ in range(K):
    bag.append(int(read()))
bosuk.sort(key=lambda x : x[0])
bag.sort()
boi = 0 # bosuk index
bheap = [] # bosuk heap
for b in bag:
    # 용량이 작은 bag부터
    while (boi<N and b>=bosuk[boi][0]):
        # 나보다 용량 작은애는 힙에 다담아
        heappush(bheap,[-bosuk[boi][1],bosuk[boi][0]])
        boi += 1
    if (bheap):
        v,_ = heappop(bheap) # 제일 가격 쎈애
        ans += -v
print(ans)
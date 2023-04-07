import sys, heapq; input=sys.stdin.readline

N = int(input())
lectures = []

for _ in range(N):
    n, start, end = map(int,input().split())
    heapq.heappush(lectures,(start,1))
    heapq.heappush(lectures,(end,-1))

ans,need = 0,0
while lectures:
    time, is_start = heapq.heappop(lectures)
    need += is_start
    ans = max(ans,need)

print(ans)
import sys;read=sys.stdin.readline
import heapq
n = int(read())
arr = []
for _ in range(n):
    deadline, cupNoodle = map(int, read().split())
    arr.append((deadline, cupNoodle))

# deadlin별 sort
arr.sort()

heap = []
for deadline,cupNoodle in arr:
    heapq.heappush(heap, cupNoodle)
    if deadline < len(heap):
        # 만약 데드라인 안에 모든걸 못끝내면 컵라면 가장 적게주는 일 삭제
        heapq.heappop(heap)
    
print(sum(heap))
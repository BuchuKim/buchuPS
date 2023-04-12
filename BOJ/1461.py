import sys;read=sys.stdin.readline
from heapq import heappop, heapify, heappush
n,m = map(int,read().split())
books = list(map(int,read().split()))
posheap = []
negheap = []
absmax = 0
for i in range(n):
    if (abs(books[i])>abs(absmax)):
        absmax = books[i]
    if (books[i]>0):
        posheap.append(-books[i])
    else:
        negheap.append(books[i])

# max처리
ans = abs(absmax)
if absmax>0:
    for _ in range(m):
        if not posheap:
            break
        posheap.remove(min(posheap))
else:
    for _ in range(m):
        if not negheap:
            break
        negheap.remove(min(negheap))

heapify(posheap)
heapify(negheap)

while posheap:
    ans += (-heappop(posheap)) * 2
    for _ in range(m-1):
        if not posheap:
            break
        heappop(posheap)
while negheap:
    ans += (-heappop(negheap)) * 2
    for _ in range(m-1):
        if not negheap:
            break
        heappop(negheap)
print(ans)
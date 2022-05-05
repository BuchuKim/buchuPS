import sys;read=sys.stdin.readline
from heapq import heappop,heappush,heapify
N = int(read())
leftheap=[] # center보다 작은값 -> 가장 큰 애가 pop
rightheap=[] # center보다 큰 값 -> 가장 작은 애가 pop
center = int(read())
print(center)
for _ in range(N-1):
    n = int(read())
    if n>center:
        heappush(rightheap,n)
        heappush(leftheap,-center)
        if (len(leftheap)==len(rightheap)):
            center = -heappop(leftheap)
        else:
            center = heappop(rightheap)
    elif n<center:
        heappush(leftheap,-n)
        heappush(rightheap,center)
        if len(leftheap)==len(rightheap):
            center = -heappop(leftheap)
        else:
            center = heappop(rightheap)
    else:
        if len(leftheap)==len(rightheap):
            heappush(rightheap,center)
        else:
            heappush(leftheap,-center)
    print(center)

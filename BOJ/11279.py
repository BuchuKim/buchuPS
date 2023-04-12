"""
from sys import stdin
from collections import deque
heap = deque([0])
def insert(N):
    # 가장 끝에 N을 넣는다. 차근차근 올라오면돼
    heap.append(N)
    i = len(heap)-1
    while i>1:
        if heap[i]>heap[i//2]:
            temp = heap[i//2]
            heap[i//2] = heap[i]
            heap[i] = temp
            i = i//2
        else:
            break
def out():
    answer = heap[1]
    if (len(heap)==2):
        heap.pop()
        return answer
    heap[1] = heap.pop()
    tmp = heap[1]
    parent = 1
    child = 2
    while (child<len(heap)):
        if (child+1<len(heap) and heap[child]<heap[child+1]):
            child = child+1
        if (heap[child]<=tmp):
            break
        heap[parent] = heap[child]
        heap[child] = tmp
        parent = child
        child *= 2
    return answer


n = int(stdin.readline())
for _ in range(n):
    c = int(stdin.readline())
    if (c==0):
        if (len(heap)==1):
            print(0)
        else:
            print(out())
    else:
        insert(c)
"""

from sys import stdin
import heapq
heap = []
n = int(stdin.readline())
for _ in range(n):
    c = int(stdin.readline())
    if (c==0):
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(heap,[-c,c])
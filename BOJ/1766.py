import sys;read=sys.stdin.readline
from heapq import heappush,heappop
from collections import deque
N,M = map(int,read().split())
graph=[[] for _ in range(N+1)]
parent = [0] * (N+1)
solved = [False] * (N+1)
answer = []
for _ in range(M):
    before,after = map(int,read().split())
    heappush(graph[before],after)
    parent[after] += 1
def search(V):
    global solved, answer
    heap = []
    for v in V:
        heappush(heap,v)
        solved[v] = True
    while heap:
        v = heappop(heap)
        for i in graph[v]:
            # v를 풀면 풀 수 있는 애들은 다 집어넣는다...
            if not solved[i]:
                parent[i] -= 1
                if (parent[i]==0):
                    heappush(heap,i)
                    solved[i] = True
        answer.append(v)
Vs=[]
for i in range(1,N+1):
    if parent[i]==0:
        Vs.append(i)
search(Vs)
for i in answer:
    print(i,end=' ')
print()
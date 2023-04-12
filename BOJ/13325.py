import sys;input=sys.stdin.readline
from collections import deque
n = int(input())
edges = [0,0]+list(map(int,input().split()))
# 일단 최대 가중치 확인
Q = deque([[1,0]])
tree_len = 0
while Q:
    i,c = Q.popleft()
    tree_len = max(c,tree_len)
    if 2*i<len(edges):
        Q.append([2*i,c+edges[2*i]])
        Q.append([2*i+1,c+edges[2*i+1]])
# 리프부터 시작해서, 부족한 숫자를 하나씩 올려!
scarce = [100000] * len(edges)
def search(v,cost):
    if 2*v<len(edges):
        search(2*v,cost+edges[2*v])
        search(2*v+1,cost+edges[2*v+1])
        scarce[v] = min(scarce[2*v],scarce[2*v+1],scarce[v])
    else:
        scarce[v] = tree_len-cost
search(1,0)
ans = 0
def spread(v,added):
    global ans
    edges[v] += scarce[v]
    ans += edges[v]
    if 2*v<len(edges):
        scarce[2*v] -= scarce[v]+added
        scarce[2*v+1] -= scarce[v]+added
        spread(2*v,scarce[v]+added)
        spread(2*v+1,scarce[v]+added)
spread(1,0)
print(ans)
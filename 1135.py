import sys;input=sys.stdin.readline
from collections import deque
n = int(input())
parents = list(map(int,input().split()))
tree = [[] for _ in range(n)]
for i in range(1,n):
    tree[parents[i]].append(i)

# time[i] : i를 루트로 하는 서브트리에 정보를 모두 전달하는데 걸리는 시간
time = [-1 for _ in range(n)]
def search(N):
    if not tree[N]:
        time[N] = 0
        return
    children_t = []
    for child in tree[N]:
        search(child)
        children_t.append(time[child])
    # 오래 걸리는 애들부터.
    children_t.sort(reverse=True)
    need_time = [children_t[i]+i+1 for i in range(len(children_t))]
    time[N] = max(need_time)
search(0)
print(time[0])
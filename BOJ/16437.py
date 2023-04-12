import sys;input=sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
isWolf = [False for _ in range(n+1)]
nums = [0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
for i in range(2,n+1):
    t,a,p = input().rstrip().split()
    if t=="W":
        isWolf[i] = True
    nums[i] = int(a)
    graph[int(p)].append(i)

visited = [False for _ in range(n+1)]
def search(v):
    global visited
    ans = 0
    visited[v] = True
    for nei in graph[v]:
        if not visited[nei]:
            ans += search(nei)
    if isWolf[v]:
        ans -= nums[v]
        if ans<0:
            return 0
    else:
        ans += nums[v]
    return ans

print(search(1))
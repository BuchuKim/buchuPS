import sys;read=sys.stdin.readline
from collections import deque
n = int(read())
friend = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int,read().split())
    friend[a].append(b)
    friend[b].append(a)
visited = [0 for _ in range(n+1)]
# dp[i][0] : i가 얼라어답터가 아닐때 필요한 얼리어답터 수
# dp[i][1] : i가 얼리어답터일때 필요한 얼리어답터 수
dp = [[0,0] for _ in range(n+1)]
def search(V):
    visited[V] = 1
    dp[V][1] = 1
    for i in friend[V]:
        if visited[i]==0:
            search(i)
            dp[V][0] += dp[i][1]
            dp[V][1] += min(dp[i][0],dp[i][1])
search(1)
print(min(dp[1][0],dp[1][1]))
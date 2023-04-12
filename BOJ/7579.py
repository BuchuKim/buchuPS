# M만큼의 메모리를 확보해야함. cost 최소
import sys;read=sys.stdin.readline
N,M = map(int,input().split())
mem = list(map(int,input().split()))
cost = list(map(int,input().split()))
c = sum(cost)
ans = c
# dp[i][j] : i번째 앱까지 살펴보았을 때, j 코스트로 얻을 수 있는 최대 바이트
dp = [[0 for _ in range(c+1)] for _ in range(N+1)]
for i in range(1,N+1):
    for j in range(1,c+1):
        if (cost[i-1]>j):
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-cost[i-1]]+mem[i-1])
        if (dp[i][j]>=M):
            ans = min(j,ans)
print(ans)
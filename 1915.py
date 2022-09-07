import sys;input=sys.stdin.readline

n,m = map(int,input().split())
dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
li = []
for _ in range(n):
    li.append(list(map(int,(list(input().rstrip())))))

ans = 0
for i in range(1,n+1):
    for j in range(1,m+1):
        if li[i-1][j-1]==0:
            continue
        dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
        ans = max(ans,dp[i][j])
print(ans**2)
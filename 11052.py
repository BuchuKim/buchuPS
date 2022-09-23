import sys;input=sys.stdin.readline
n = int(input())
p = [0]+list(map(int,input().split()))
# dp[a][b] : a번째 카드팩까지 살펴봤을 때, b개를 구성하기 위한 최대 비용
dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
dp[1] = [p[1]*i for i in range(n+1)]
for i in range(2,n+1):
    for j in range(n+1):
        cur = j//i
        for k in range(cur+1):
            dp[i][j] = max(dp[i][j],dp[i-1][j],dp[i-1][j-k*i]+p[i]*k)
print(dp[n][n])
import sys;input=sys.stdin.readline
n = int(input())
if n==1:
    print(3)
    exit()
# dp[a][b][c] : a일에 결석을 b번 연속으로 했고 c번 지각함
dp = [[[0,0] for _ in range(3)] for _ in range(n)]
dp[0][0][0],dp[0][0][1],dp[0][1][0] = 1,1,1
dp[1][0][0],dp[1][0][1],dp[1][1][0],dp[1][1][1],dp[1][2][0] = 2,3,1,1,1
for i in range(2,n):
    dp[i][0][0] = dp[i-1][0][0]+dp[i-1][2][0]+dp[i-1][1][0]
    dp[i][0][1] = (dp[i-1][0][0]+dp[i-1][1][0]+dp[i-1][2][0])+(dp[i-1][0][1]+dp[i-1][2][1]+dp[i-1][1][1])
    dp[i][1][0] = dp[i-1][0][0]
    dp[i][1][1] = dp[i-1][0][1]
    dp[i][2][0] = dp[i-1][1][0]
    dp[i][2][1] = dp[i-1][1][1]
ans = 0
for i in range(3):
    for j in range(2):
        ans += dp[-1][i][j]
print(ans%1000000)
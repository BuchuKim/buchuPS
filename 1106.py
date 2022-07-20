import sys;read=sys.stdin.readline
from math import ceil
c,n = map(int,read().split())
method = []
for _ in range(n):
    cost,customer = map(int,read().split())
    method.append([cost,customer])
# dp[i][j] : i번째 도시까지 살펴봤을 때 j명을 넘기기 위한 최소 비용.
dp = [[sys.maxsize for _ in range(c+1)] for _ in range(n+1)]
dp[0][0] = 0
for i in range(1,n+1):
    for j in range(c+1):
        cost, customer = method[i-1]
        time = ceil(j/customer)
        dp[i][j] = min(dp[i-1][j],time*cost)
        k=0
        while j-k*customer>=0:
            # i번 지역에 홍보를 돌지 않거나
            # i번 지역에 홍보를 k번 돌거나.
            dp[i][j] = min(dp[i-1][j-k*customer]+k*cost,dp[i][j])
            k+=1
print(dp[n][c])
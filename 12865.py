# 무게 W, 가치 V, 최대 K, N개 물건
import sys
read=sys.stdin.readline
N,K = map(int,read().split())
thing = [[0,0]]
for _ in range(N):
    thing.append(list(map(int,read().split())))
# dp[n][k] : n번째 물건까지 살펴봤을 때, 크기가 k인 가방의 최대 가치
dp = [[0 for _ in range(K+1)] for _ in range(N+1)]
for i in range(1,N+1):
    for j in range(1,K+1): # 각각의 가방에 대하여~
        w = thing[i][0]
        v = thing[i][1]
        # 1. 넣을 물건의 무게가 더 크다면 넣지 않음
        # j:가방의 크기, w:넣을 물건의 무게, v:넣을 물건의 가치
        if (w>j):
            dp[i][j] = dp[i-1][j]
        else:
            # 2. 현재물건을 넣기 위해 빼든가 / 빼지않고 그대로 가지고 가든가.
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-w]+v)
print(dp[N][K])
import sys;read=sys.stdin.readline
N = int(read())
nums = list(map(int,read().split()))
# dp[a][b] : a~b가 팰린드롬인지?
dp = [[0]*N for _ in range(N)]
for interval in range(N):
    for s in range(N):
        e = s+interval
        if (e>=N):
            break
        if (s==e):
            dp[s][e] = 1
            continue
        if (s+1==e):
            if nums[s]==nums[e]:
                dp[s][e] = 1
            continue
        if (nums[s]==nums[e] and dp[s+1][e-1]==1):
            dp[s][e] = 1
M = int(read())
print(dp)
for _ in range(M):
    s,e = map(int,read().split())
    print(dp[s-1][e-1])
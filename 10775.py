import sys;read=sys.stdin.readline
G = int(read())
# dp[i] : gate번호가 i 이하인 gate중 가능한 가장 높은 gate
dp = [i for i in range(G+1)]
isFull = [False] * (G+1)
P = int(read())
ans = 0
for _ in range(P):
    g = int(read())
    # dp[g]에 비행기를 도킹시킬거다.
    target = g
    while (dp[target]!=target):
        dp[target] = dp[dp[target]]
        target = dp[target]
    if (target==0):
        print(ans)
        exit()
    dp[target] -= 1
    dp[g] = target - 1
    ans += 1
print(ans)
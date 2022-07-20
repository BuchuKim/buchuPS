import sys;input=sys.stdin.readline
dp = [10**15 for _ in range(100)]
dp[0] = 0
for coin in [1,10,25]:
        for i in range(coin,100):
            dp[i] = min(dp[i],dp[i-coin]+1)
for _ in range(int(input())):
    price = int(input())
    ans = 0
    while price>0:
        ans += dp[price%100]
        price //= 100
    print(ans)
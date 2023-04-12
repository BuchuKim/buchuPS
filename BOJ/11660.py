from sys import stdin; read=stdin.readline
N,M = map(int,read().split())
dp = []
for _ in range(N):
    li = list(map(int,read().split()))
    d = [li[0]]
    for i in range(1,N):
        d.append(li[i]+d[i-1])
    dp.append(d)
for _ in range(M):
    x1,y1,x2,y2 = map(int,read().split())
    ans = 0
    for i in range(x1-1,x2):
        if (y1!=1):
            ans += dp[i][y2-1] - dp[i][y1-2]
        else:
            ans += dp[i][y2-1]
    print(ans)
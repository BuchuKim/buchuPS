import sys;read=sys.stdin.readline

T = int(read())

dp0 = [0 for _ in range(41)]
dp1 = [0 for _ in range(41)]

dp0[0] = 1
dp1[1] = 1
dp1[1] = 1

for i in range(2,41):
    dp0[i] = dp0[i-1]+dp0[i-2]
    dp1[i] = dp1[i-1]+dp1[i-2]

for _ in range(T):
    N = int(read())
    print(dp0[N], dp1[N])
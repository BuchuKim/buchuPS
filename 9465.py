import sys;read=sys.stdin.readline

for _ in range(int(read())):
    n = int(read())
    dp1 = [0 for _ in range(n)]
    dp2 = [0 for _ in range(n)]
    s1 = list(map(int,read().split()))
    s2 = list(map(int,read().split()))
    if n==1:
        print(max(s1[0],s2[0]))
        continue
    dp1[0] = s1[0]
    dp2[0] = s2[0]
    dp1[1] = s1[1] + s2[0]
    dp2[1] = s2[1] + s1[0]
    for i in range(2,n):
        dp1[i] = max(dp2[i-1],dp2[i-2],dp1[i-2]) + s1[i]
        dp2[i] = max(dp1[i-1],dp1[i-2],dp2[i-2]) + s2[i]
    print(max(dp1[-1],dp2[-1]))
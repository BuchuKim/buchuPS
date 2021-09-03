import sys;read=sys.stdin.readline
N = int(read())
li = list(map(int,read().split()))
dp1 = [1 for _ in range(N)]
dp2 = [1 for _ in range(N)]
for i in range(1,N):
    j = i-1
    while (j>=0):
        if (li[j]<li[i]):
            dp1[i] = max(dp1[i],dp1[j]+1)
        j -= 1
i = N-2
while (i>=0):
    j = i+1
    while (j<N):
        if (li[j]<li[i]):
            dp2[i] = max(dp2[i],dp2[j]+1)
        j += 1
    i -=1
dp = [dp1[i]+dp2[i] for i in range(N)]
print(max(dp)-1)
import sys;read=sys.stdin.readline
n,m = map(int,read().split())
a = list(map(int,read().split()))
b = list(map(int,read().split()))
a.sort()
b.sort()

if n>m:
    temp = n
    n = m
    m = temp
    temp = a
    a = b
    b = temp

# dp[a][b] : a까지 살펴봤을 때, a->b최솟값
dp = [[sys.maxsize for _ in range(m)] for _ in range(n)]
dp[0] = [abs(a[0]-b[i]) for i in range(m)]
for i in range(1,n):
    for j in range(i,m):
        dp[i][j] = abs(a[i]-b[j]) + min(dp[i-1][:j])
print(min(dp[-1]))
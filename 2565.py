import sys;input=sys.stdin.readline
n = int(input())
line = []
for _ in range(n):
    a,b = map(int,input().split())
    line.append([a,b])
line.sort(key=lambda x : x[0])
b,dp = [],[1 for _ in range(n)]
for i in range(n):
    b.append(line[i][1])
for i in range(1,n):
    for j in range(i):
        if b[j]<b[i]:
            dp[i] = max(dp[i],dp[j]+1)
print(n-max(dp))
import sys;input=sys.stdin.readline
n = int(input())
dp = [0,0,3,0]
for i in range(4,n+1):
    if i%2==1:
        dp.append(0)
    else:
        dp.append(dp[i-2]*3+sum(dp[:i-2])*2 + 2)
print(dp[n])
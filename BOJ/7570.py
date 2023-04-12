# 가장 긴 증가하는 부분수열인 것 같은데 연속으로 증가해야함
import sys;input=sys.stdin.readline
n = int(input())
children = list(map(int,input().split()))
appear = [0 for _ in range(n+1)]
dp = [1 for _ in range(n+1)]
max_inc = 0
for i in range(n):
    appear[children[i]] = 1
    if children[i]==1:
        continue
    if appear[children[i]-1]==1:
        dp[children[i]] = dp[children[i]-1]+1
        max_inc = max(max_inc,dp[children[i]])
print(n-max_inc)
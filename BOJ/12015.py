import sys;read=sys.stdin.readline
from bisect import bisect_left
N = int(read())
nums = list(map(int,read().split()))
dp = []
for n in nums:
    index = bisect_left(dp,n)
    if (index>=len(dp)):
        dp.append(n)
    else:
        dp[index]=n
print(len(dp))
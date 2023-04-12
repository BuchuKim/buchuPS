import sys
from collections import deque
a = deque()
a[-1]
read = sys.stdin.readline
_ = read().split()
li = list(map(int,read().split()))
dp = [1] * len(li) # 그 index를 포함한 길이
for i in range(len(li)):
    j = i - 1
    while (j>=0):
        if (li[j]<li[i]):
            dp[i] = max(dp[i],dp[j]+1)
        j -= 1
print(max(dp))
import sys;read=sys.stdin.readline
from collections import defaultdict
N,S = map(int,read().split())
nums = list(map(int,read().split()))
nums.sort()
start = 0
end = N-1
answer = 0
while start<end:
    hap = sum(nums[start:end+1])
    if hap==S:
        answer += 1
        start += 1
    elif hap<S:
        start += 1
    else:
        end -= 1
print(answer)
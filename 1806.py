import sys;read=sys.stdin.readline
n,s = map(int,read().split())
nums = [0]+list(map(int,read().split()))
for i in range(1,len(nums)):
    nums[i] += nums[i-1]
answer = 100001
start = 0
end = 1
while start<n:
    if nums[end]-nums[start]>=s:
        answer = min(answer,end-start)
        start += 1
    else:
        if end<n:
            end += 1
        else:
            start += 1
if answer==100001:
    print(0)
else:
    print(answer)
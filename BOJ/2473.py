import sys;read=sys.stdin.readline
n = int(read())
nums = list(map(int,read().split()))
nums.sort()
temp = 5000000000
ans = [0,0,0]
for i in range(n-2):
    cur = nums[i]
    start = i+1
    end = n-1
    while (start<end):
        if i>0 and cur==nums[i-1]:
            continue
        s = cur+nums[start]+nums[end]
        if (abs(s)<temp):
            temp = abs(s)
            ans = [cur,nums[start],nums[end]]
        if s<0:
            start += 1
        elif s>0:
            end -= 1
        elif s==0:
            print(ans[0],ans[1],ans[2])
            sys.exit(0)
print(ans[0],ans[1],ans[2])
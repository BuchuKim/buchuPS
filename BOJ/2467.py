import sys;read=sys.stdin.readline
from bisect import bisect_left, bisect_right
N = int(read())
nums = list(map(int,read().split()))
i = bisect_left(nums,0)
if (i==0 or N==2):
    # 전체가 양수
    print(nums[0],nums[1])
    exit()
elif (i>=N):
    # 전체가 음수
    print(nums[-2],nums[-1])
    exit()

# find... from left
l = 0
pos = nums[i:]
ans = 1000000000
ans_pair = [0,0]
while (l<i):
    r = bisect_left(nums,-nums[l]) # 절댓값이 l이상인 것 중 가장 작은 수의 index
    if (r==N):
        r -= 1
    if (abs(nums[l]+nums[r])<ans):
        ans = abs(nums[l]+nums[r])
        ans_pair = [l,r]
    if (r-1>=i and abs(nums[l]+nums[r-1])<ans):
        ans = abs(nums[l]+nums[r-1])
        ans_pair = [l,r-1]
    l+=1
    
# 산성/ 알칼리성 용액만으로도 할 수 있는지?
if (i<N-1):
    if (nums[i]+nums[i+1]<ans):
        ans_pair = [i,i+1]
if (i>1):
    if (abs(nums[i-2]+nums[i-1])<ans):
        ans_pair = [i-2,i-1]
print(nums[ans_pair[0]],nums[ans_pair[1]])
import sys;input=sys.stdin.readline
from copy import deepcopy
n = int(input())
current = list(map(int,input().rstrip()))
target = list(map(int,input().rstrip()))

# 1. 첫 전구를 바꾸는 경우
case1,a1 = deepcopy(current),1
case1[0] = 1-current[0]
case1[1] = 1-current[1]

# 2. 첫 전구를 바꾸지 않는 경우
case2,a2 = deepcopy(current),0

for i in range(1,n):
    if case1[i-1]!=target[i-1]:
        a1 += 1
        case1[i-1] = 1-case1[i-1]
        case1[i] = 1-case1[i]
        if i<n-1:
            case1[i+1] = 1-case1[i+1]
    if case2[i-1]!=target[i-1]:
        a2 += 1
        case2[i-1] = 1-case2[i-1]
        case2[i] = 1-case2[i]
        if i<n-1:
            case2[i+1] = 1-case2[i+1]

if case1[-1]!=target[-1] and case2[-1]!=target[-1]:
    print(-1)
else:
    ans = n
    if case1[-1]==target[-1]:
        ans = a1
    if case2[-1]==target[-1]:
        ans = min(ans,a2)
    print(ans)

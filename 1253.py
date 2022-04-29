import sys;read=sys.stdin.readline
from itertools import combinations
n = int(read())
arr = list(map(int,read().split()))

# corner case
if (n==1 or n==2):
    print(0)
    exit()

arr.sort()
ans = 0
for i in range(n):
    l,r = 0,n-1
    good = False
    while (l<r):
        if (l==i):
            l += 1
            continue
        if (r==i):
            r -= 1
            continue
        if (arr[l]+arr[r]<arr[i]):
            l += 1
        elif (arr[l]+arr[r]>arr[i]):
            r -= 1
        else:
            good = True
            break
    if (good):
        ans += 1
print(ans)
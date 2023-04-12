import sys;read=sys.stdin.readline
from collections import defaultdict
T = int(read())
N = int(read())
A = list(map(int,read().split()))
M = int(read())
B = list(map(int,read().split()))
sum_a = defaultdict(int)
sum_b = defaultdict(int)
for i in range(N):
    for j in range(i,N):
        sum_a[sum(A[i:j+1])] += 1
for i in range(M):
    for j in range(i,M):
        sum_b[sum(B[i:j+1])] += 1
ans = 0
for key in sum_a.keys():
    ans += sum_a[key]*sum_b[T-key]
print(ans)
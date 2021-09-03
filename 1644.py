import sys;read=sys.stdin.readline
from math import sqrt
N = int(read())
# 에라토스 어쩌구
sosu = [True] * (N+1)
sosu[0] = False
sosu[1] = False
snums = [] # n 이하의 소수들을 저장한 list
for i in range(2,int(sqrt(N))+1):
    if sosu[i]==True:
        for j in range(i+i,N+1,i):
            sosu[j] = False
for i in range(len(sosu)):
    if sosu[i]:
        snums.append(i)
ans = 0
start = 0
hap = 0
while start<len(snums):
    for i in range(start,len(snums)):
        if (hap==N):
            ans += 1
            start += 1
            hap = 0
            break
        elif (hap>N):
            start += 1
            hap = 0
            break
        hap += snums[i]
print(ans)

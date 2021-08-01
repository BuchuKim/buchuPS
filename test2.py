# n: 수의 갯수, m : 합을 구해야하는 횟수..?
from sys import stdin
n,m = map(int,stdin.readline().split())
Ns = list(map(int,stdin.readline().split()))
for i in range(1,n):
    Ns[i] = Ns[i] + Ns[i-1]
for _ in range(m):
    i,j = map(int,stdin.readline().split())
    if (i==1):
        print(Ns[j-1])
    else:
        print(Ns[j-1]-Ns[i-2])
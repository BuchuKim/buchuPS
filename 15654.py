import sys; read=sys.stdin.readline
from itertools import permutations
N,M = map(int,read().split())
li = list(map(int,read().split()))
li.sort()
c = permutations(li,M)
for t in c:
    for num in t:
        print(num,end=' ')
    print()
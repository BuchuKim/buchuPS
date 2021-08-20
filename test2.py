import sys
from itertools import combinations_with_replacement
read=sys.stdin.readline
N,M = map(int,read().split())
li = list(map(int,read().split()))
li.sort()
com = combinations_with_replacement(li,M)
for c in com:
    for i in c:
        print(i,end=' ')
    print()
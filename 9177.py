import sys;input=sys.stdin.readline
from collections import deque
for i in range(int(input())):
    a,b,c = input().split()
    success = False
    i3 = 0
    Q = deque([(0,0)])
    visited = [[0 for _ in range(len(b)+1)] for _ in range(len(a)+1)]
    while Q:
        for _ in range(len(Q)):
            i1,i2 = Q.popleft()
            if i1<len(a) and visited[i1+1][i2]==0 and a[i1]==c[i3]:
                Q.append((i1+1,i2))
                visited[i1+1][i2] = 1
            if i2<len(b) and visited[i1][i2+1]==0 and b[i2]==c[i3]:
                Q.append((i1,i2+1))
                visited[i1][i2+1] = 1
        i3 += 1
    if i3==len(c)+1:
        success = True
    if success:
        print('Data set {0}: yes'.format(i+1))
    else:
        print('Data set {0}: no'.format(i+1))
from sys import stdin
from collections import deque
def DSLR(n):
    d = n*2
    if (d>9999):
        d = d%10000
    s = n - 1
    if (n==0):
        s = 9999
    a = str(n)
    l = int(a[1:]+a[0])
    r = int(a[-1]+a[:-1])
    return d,s,l,r
def search(a,b):
    visited = [0 for _ in range(10000)]
    bfsQ = deque([[a,'']])
    visited[a] = 1
    while (len(bfsQ)>0):
        a = bfsQ.popleft()
        d,s,l,r = DSLR(a[0])
        if (visited[d]==0):
            if (d==b):
                return a[1]+'D'
            bfsQ.append([d,a[1]+'D'])
        if (visited[s]==0):
            if (s==b):
                return a[1]+'S'
            bfsQ.append([s,a[1]+'S'])
        if (visited[l]==0):
            if (l==b):
                return a[1]+'L'
            bfsQ.append([l,a[1]+'L'])
        if (visited[r]==0):
            if (r==b):
                return a[1]+'R'
            bfsQ.append([r,a[1]+'R'])
T = int(stdin.readline())
for _ in range(T):
    A,B = map(int,stdin.readline().split())
    print(search(A,B))
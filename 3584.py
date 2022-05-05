import sys;read=sys.stdin.readline
from collections import deque
def route(a,parents):
    ret = deque()
    while (parents[a]!=a):
        ret.append(a)
        a = parents[a]
    ret.append(a)
    return ret
for _ in range(int(read())):
    n = int(read())
    parent = [i for i in range(n+1)]
    for _ in range(n-1):
        p,c = map(int,read().split())
        parent[c] = p
    a,b = map(int,read().split())
    if (a==b):
        print(a)
        continue
    # a부터 ~ 조상까지
    a_route = route(a,parent)
    b_route = route(b,parent)
    # 가장 처음 pop : 공통조상
    ans = a_route.pop()
    b_route.pop()
    while a_route and b_route:
        a = a_route.pop()
        b = b_route.pop()
        if (a!=b):
            break
        ans = a
    print(ans)
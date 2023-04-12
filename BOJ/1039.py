import sys;input=sys.stdin.readline
from collections import deque
n,k = map(int,input().split())
Q = deque()
can = False
ans = 0
visited = [[0 for _ in range(k+1)] for _ in range(1000001)]
Q.append([str(n),0])
visited[n][0] = 1
while Q:
    s,cnt = Q.popleft()
    if cnt==k:
        can = True
        ans = max(int(s),ans)
        continue
    for i in range(len(s)-1):
        for j in range(i+1,len(s)):
            if i==0 and s[j]=='0':
                continue
            n_n = s[:i]+s[j]+s[i+1:j]+s[i]+s[j+1:]
            if visited[int(n_n)][cnt+1]==0:
                visited[int(n_n)][cnt+1] = 1
                Q.append([n_n,cnt+1])
if can:
    print(ans)
else:
    print(-1)
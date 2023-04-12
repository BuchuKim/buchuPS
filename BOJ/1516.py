import sys;read=sys.stdin.readline
from collections import deque

n = int(read())
# required[i] : i번 건물이 지어져야 지을 수 있는 애들
required = [[] for _ in range(n)]
# parent : i번 건물을 짓기 위해 필요한 건물 수
parent = [0 for _ in range(n)]
ans = [0 for _ in range(n)]
time = [0 for _ in range(n)]
done = deque()
for i in range(n):
    building = list(map(int,read().split()))[:-1]
    time[i] = building[0]
    parent[i] = len(building[1:])
    if len(building)==1:
        done.append(i)
        ans[i] = time[i]
    for r in building[1:]:
        required[r-1].append(i)
while done:
    n = done.popleft()
    # n번 건물이 지어지고 난 직후!
    for b in required[n]:
        parent[b] -= 1
        if parent[b]==0:
            # b는 이제 지을 수 있다
            ans[b] = max(ans[n],ans[b]) + time[b]
            done.append(b)
        else:
            ans[b] = max(ans[b],ans[n])
for i in range(len(ans)):
    print(ans[i])
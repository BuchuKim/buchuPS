import sys;read=sys.stdin.readline
from collections import deque
n,k = map(int,read().split())
sc = list(map(int,read().split()))
# 전자기기가 다음에 언제 나오는지!
next_appear = [deque() for _ in range(k+1)]
ans = 0
for i in range(k):
    next_appear[sc[i]].append(i)

# 현재 멀티탭에 꽂혀있는 애들
cur = set()
for i in range(k):
    next_appear[sc[i]].popleft()
    if not sc[i] in cur:
        # 꽂아야돼
        if len(cur)==n:
            # 뽑아야돼
            p = -1
            toDelete = 0
            for c in cur:
                if (not next_appear[c]):
                    toDelete = c
                    break
                elif (next_appear[c][0]>p):
                    p = next_appear[c][0]
                    toDelete = c
            cur.remove(toDelete)
            ans += 1
        cur.add(sc[i])
print(ans)
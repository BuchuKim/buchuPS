import sys;read=sys.stdin.readline
from collections import deque
n = int(read())
arr = list(map(int,read().split()))
delete = int(read())
root = []
children = [[] for _ in range(n)]
for i in range(n):
    parent = arr[i] # i번 노드의 부모님
    if (parent!=-1):
        children[parent].append(i)
    else:
        # 부모가 -1이면 얘는 root
        root.append(i)

children[delete] = []
if (arr[delete]!=-1):
    children[arr[delete]].remove(delete)
else:
    root.remove(delete)

ans = 0
bfsQ = deque(root)

while bfsQ:
    node = bfsQ.popleft()
    if len(children[node])==0:
        ans += 1
        continue
    for child in children[node]:
        bfsQ.append(child)
print(ans)
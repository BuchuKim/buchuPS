import sys;read=sys.stdin.readline
from collections import deque
for _ in range(int(read())):
    arr = []
    for _ in range(int(read())):
        arr.append(read().rstrip())
    arr.sort()
    arr = deque(arr)
    ans = True
    if len(arr)==1:
        print('YES')
        continue
    s = arr.popleft()
    while arr:
        if len(s)>len(arr[0]):
            s = arr.popleft()
            continue 
        if arr[0][:len(s)]==s:
            ans = False
            break
        s = arr.popleft()
    if ans:
        print('YES')
    else:
        print('NO')

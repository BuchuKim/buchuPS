import sys; read=sys.stdin.readline
from collections import deque
s = read().strip()
p = read().strip()
q = deque()
for i in range(len(s)):
    q.append(s[i])
    if (s[i]==p[-1] and len(p)<=len(q)):
        al = True
        for j in range(1,len(p)+1):
            if (q[-j]!=p[-j]):
                al = False
                break
        if al:
            for _ in range(len(p)):
                q.pop()
if (len(q)==0):
    print('FRULA')
else:
    for s in q:
        print(s,end='')
    print()
import sys;read=sys.stdin.readline
pos = []
neg = []
isZero = False
for _ in range(int(read())):
    n = int(read())
    if n>0:
        pos.append(n)
    elif n<0:
        neg.append(n)
    else:
        isZero = True
ans = 0
pos.sort(reverse=True)
neg.sort()
if len(neg)%2==1:
    if not isZero:
        ans += neg.pop()
    else:
        neg.pop()
if len(pos)%2==1:
    ans += pos.pop()
for i in range(0,len(neg),2):
    ans += neg[i]*neg[i+1]
for i in range(0,len(pos),2):
    if pos[i+1]==1:
        ans += pos[i]+pos[i+1]
    else:
        ans += pos[i]*pos[i+1]
print(ans)
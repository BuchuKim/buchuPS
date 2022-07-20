import sys;read=sys.stdin.readline
n = int(read())
m = int(read())
friend = [i for i in range(n+1)]
enemy = [[] for _ in range(n+1)]
def find(x):
    f = friend[x]
    while f!=friend[f]:
        f = friend[f]
    friend[x] = f
    return f
def union(x,y):
    x = find(x)
    y = find(y)
    if x<y:
        friend[y] = x
    else:
        friend[x] = y
for _ in range(m):
    rel,a,b = read().split()
    if rel=="F":
        union(int(a),int(b))
    else:
        enemy[int(a)].append(int(b))
        enemy[int(b)].append(int(a))
for i in range(1,n+1):
    for e in enemy[i]:
        for en in enemy[e]:
            union(i,en)
ans = 0
for i in range(1,n+1):
    find(i)
    if i==friend[i]:
        ans += 1
print(ans)
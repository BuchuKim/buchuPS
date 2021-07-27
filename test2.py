from sys import stdin
n,m = map(int,stdin.readline().split())
pocketmon = {}
for i in range(1,n+1):
    name = stdin.readline().strip()
    pocketmon[i] = name
    pocketmon[name] = i
for i in range(m):
    q = stdin.readline().strip()
    if q.isdigit():
        q = int(q)
    print(pocketmon[q])
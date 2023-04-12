import sys
N = int(sys.stdin.readline().strip())
li = list(map(int,sys.stdin.readline().split()))
co = sorted(set(li))
d = {}
for i in range(len(co)):
    d[co[i]] = i
for i in li:
    print(d[i],end=' ')
print()
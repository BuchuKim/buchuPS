import sys
read = sys.stdin.readline
N = int(read())
pa = list(map(int,read().split()))
premax = [0,0,0]
premin = [0,0,0]
curmax = [pa[0],pa[1],pa[2]]
curmin = [pa[0],pa[1],pa[2]]
for _ in range(N-1):
    premax = [i for i in curmax]
    premin = [i for i in curmin]
    a = list(map(int,read().split()))
    curmax[0] = a[0] + max(premax[0],premax[1])
    curmax[1] = a[1] + max(premax[0],premax[1],premax[2])
    curmax[2] = a[2] + max(premax[1],premax[2])
    curmin[0] = a[0] + min(premin[0],premin[1])
    curmin[1] = a[1] + min(premin[0],premin[1],premin[2])
    curmin[2] = a[2] + min(premin[1],premin[2])
print(max(curmax),min(curmin))
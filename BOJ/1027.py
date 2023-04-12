import sys;read=sys.stdin.readline
n = int(read())
building = list(map(int,read().split()))
ans = 0
def search_left(x):
    if x==0:
        return 0
    can = 0
    maxgrad = sys.maxsize
    i = x - 1
    while (i>=0):
        grad = (building[x]-building[i])/(x-i)
        # grad가 작아야지 보임
        if (grad<maxgrad):
            can += 1
            maxgrad = grad
        i -= 1
    return can
def search_right(x):
    if x==n:
        return 0
    can = 0
    maxgrad = -sys.maxsize
    for i in range(x+1,n):
        grad = (building[i]-building[x])/(i-x)
        # grad가 커야지 보임
        if (grad>maxgrad):
            can += 1
            maxgrad = grad
    return can
for i in range(n):
    ans = max(search_left(i) + search_right(i),ans)
print(ans)
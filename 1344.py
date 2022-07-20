import sys;input=sys.stdin.readline
a = int(input())/100
b = int(input())/100
sosu = [2,3,5,7,11,13,17]
def nCr(n,r):
    ret = 1
    for i in range(n,n-r,-1):
        ret *= i
    for i in range(r,0,-1):
        ret /= i
    return ret
def dokrip(n,k,p):
    return nCr(n,k) * (p**k) * ((1-p)**(n-k))
# 1-두팀이 모두 소수로 득점하지 않을 확률
ans = 0
for i in range(19):
    for j in range(19):
        if i in sosu or j in sosu:
            continue
        pa = dokrip(18,i,a)
        pb = dokrip(18,j,b)
        ans += pa*pb
print(1-ans)
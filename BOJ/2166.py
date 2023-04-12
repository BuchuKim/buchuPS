import sys;read=sys.stdin.readline
N = int(read())
x = []
y = []
for _ in range(N):
    a,b = map(float,read().split())
    x.append(a)
    y.append(b)
x.append(x[-1])
y.append(y[-1])
plus = 0.0
minus = 0.0
for i in range(N):
    plus += x[i]*y[i+1]
for i in range(1,N+1):
    minus -= x[i]*y[i-1]
print(round(abs(plus-minus)/2,1))
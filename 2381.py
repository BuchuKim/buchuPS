import sys;input=sys.stdin.readline
hap = []
cha = []
for _ in range(int(input())):
    x,y = map(int,input().split())
    hap.append(x+y)
    cha.append(x-y)
b = max(cha) - min(cha)
d = max(hap) - min(hap)
print(max(b,d))
# b >= d : (c-a) + (b-d) = (c-d) - (a-b)
# b <  d : (c-a) + (d-b) = (c+d) - (a+b)

import sys;input=sys.stdin.readline
n = int(input())
line = [0 for _ in range(2*n)]
for i in range(n):
    s,e = map(int,input().split())
    line[i]= (s,1)
    line[i+n]= (e,-1)
line.sort(key=lambda x: (x[0],x[1]))
cur = 0
ans = 0
for _,i in line:
    cur += i
    ans = max(ans,cur)
print(ans)
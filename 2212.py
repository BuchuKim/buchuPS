import sys;input=sys.stdin.readline
n = int(input())
k = int(input())
s = list(map(int,input().split()))
s.sort()
dis = []
for i in range(n-1):
    dis.append(abs(s[i]-s[i+1]))
dis.sort(reverse=True)
print(sum(dis[k-1:]))
import sys;input=sys.stdin.readline
n,c = map(int,input().split())
schedule = []
can = [c for _ in range(n+1)]
for _ in range(int(input())):
    schedule.append(list(map(int,input().split())))
schedule.sort(key=lambda x : x[1])
ans = 0
for s,e,b in schedule:
    min_vil = min(can[s:e])
    min_vil = min(min_vil,b)
    for i in range(s,e):
        can[i] -= min_vil
    ans += min_vil
print(ans)
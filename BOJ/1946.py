import sys;input=sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    ans,rank,worst_b = 0, [], N+1
    for i in range(N):
        rank.append(list(map(int,input().split())))
    rank.sort()
    for a,b in rank:
        if b<worst_b:
            ans += 1
            worst_b = b
    print(ans)

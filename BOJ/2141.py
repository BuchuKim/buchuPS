import sys;input=sys.stdin.readline
n = int(input())
town = []
total = 0
for i in range(n):
    x,a = map(int,input().split())
    town.append([x,a])
    total += a
town.sort(key=lambda x:(x[0]))
nujeok = 0
for i in range(n):
    nujeok += town[i][1]
    if nujeok >= total/2:
        print(town[i][0])
        exit()
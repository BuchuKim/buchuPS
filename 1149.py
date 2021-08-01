from sys import stdin
N = int(stdin.readline())
cost = []
for _ in range(N):
    cost.append(list(map(int,stdin.readline().split())))
# 0~N-1번까지 집을 .. 계산하자. r[i] : i번째 집을 r로 칠했을 때 최소비용
r = [cost[0][0]]
g = [cost[0][1]]
b = [cost[0][2]]
for i in range(1,N):
    r.append(min(g[i-1],b[i-1])+cost[i][0])
    g.append(min(r[i-1],b[i-1])+cost[i][1])
    b.append(min(r[i-1],g[i-1])+cost[i][2])
print(min(r[-1],g[-1],b[-1]))
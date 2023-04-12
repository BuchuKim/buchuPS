# 11047 동전 0
# 동전 갯수는 무한하다고 가정!
N,K = map(int,input().split())
coins = []
for _ in range(N):
    coins.append(int(input()))

answer = 0
g = 0 # greedy index
while (g<len(coins)-1 and coins[g+1]<=K):
    g += 1
while (K>0):
    cur = K//coins[g] # 현재 들어갈 동전 갯수
    K -= cur * coins[g]
    answer += cur
    g -= 1

print(answer)
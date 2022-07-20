import sys;input=sys.stdin.readline
n = int(input())
tree = [[] for _ in range(n+1)]
w = [0]+list(map(int,input().split()))
for _ in range(n-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

# dp[i][0] : i번이 독립집합에 포함되지 않았을 때 최대
# dp[i][1] : i번이 독립집합에 포함되었을 때 최대
# dp[i][2] : i번이 독립집합에 포함 안되었을 때 nodes
# dp[i][3] : i번이 독립집합에 포함되었을 때 nodes
visited = [False for _ in range(n+1)]
dp = [[0,w[i],[],[]] for i in range(n+1)]
def search(v):
    visited[v] = True
    dp[v][3].append(v)
    for nei in tree[v]:
        if not visited[nei]:
            search(nei)
            # v가 독립집합이면 nei는 독립집합에 포함되어선 안돼!
            dp[v][1] += dp[nei][0]
            for i in dp[nei][2]:
                dp[v][3].append(i)
            # v가 독립집합이 아니면 더 최적의 nei를 뽑을거다.
            if dp[nei][1]>dp[nei][0]:
                dp[v][0] += dp[nei][1]
                for i in dp[nei][3]:
                    dp[v][2].append(i)
            else:
                dp[v][0] += dp[nei][0]
                for i in dp[nei][2]:
                    dp[v][2].append(i)

search(1)
if dp[1][0]>dp[1][1]:
    print(dp[1][0])
    dp[1][2].sort()
    print(*dp[1][2])
else:
    print(dp[1][1])
    dp[1][3].sort()
    print(*dp[1][3])
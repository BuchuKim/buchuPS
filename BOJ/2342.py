import sys;read=sys.stdin.readline
arr = list(map(int,read().split()))[:-1]
MAX = 500000

# corner case
if (len(arr)==0):
    print(0)
    exit()

def cost(s,e):
    if (s==0):
        return 2
    elif (abs(s-e)==2):
        return 4
    elif (s==e):
        return 1
    else:
        return 3

# dp[i][l][r] : i번째 움직임을 (l,r)로 수행했을 때 드는 비용의 총합
dp = [[[MAX for _ in range(5)] for _ in range(5)] for _ in range(len(arr))]

# base case
dp[0][arr[0]][0] = 2
dp[0][0][arr[0]] = 2

for i in range(1,len(arr)): # 모든 움직임에 대하여..
    for j in range(5): # 오른발 고정
        for k in range(5): # 왼발 index
            # 왼발이 arr[i]로 이동함!
            dp[i][arr[i]][j] = min(dp[i][arr[i]][j],dp[i-1][k][j]+cost(k,arr[i]))
    for j in range(5): # 왼발 고정
        for k in range(5): # 오른발 index
            # 오른발이 arr[i]로 이동함
            dp[i][j][arr[i]] = min(dp[i][j][arr[i]],dp[i-1][j][k]+cost(k,arr[i]))

ans = MAX
for i in range(5):
    for j in range(5):
        ans = min(ans,dp[-1][i][j])
print(ans)
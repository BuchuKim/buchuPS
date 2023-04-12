import sys;input=sys.stdin.readline
n = int(input())
w = int(input())
# dp[w][i][0] : w번 사건을 i번 경찰차가 처리했을 때 비용
# dp[w][i][1] : w번 사건을 i번 경찰차가 처리했을 때 1번 경찰차의 위치
# dp[w][i][2] : w번 사건을 i번 경찰차가 처리했을 때 2번 경찰차의 위치
# dp[w][i][3] : w번 사건을 i번 경찰차가 처리했을 때 path
dp = [[[0,[1,1],[n,n],[]] for _ in range(2)] for _ in range(w+1)]
path = [[],[]]
for i in range(1,w+1):
    a,b = map(int,input().split())
    dp[i][0][0] = min(abs(a-dp[i-1][0][1][0])+abs(b-dp[i-1][0][1][1])+dp[i-1][0][0],abs(a-dp[i-1][1][1][0])+abs(b-dp[i-1][1][1][1])+dp[i-1][1][0])
    if dp[i][0][0]==abs(a-dp[i-1][0][1][0])+abs(b-dp[i-1][0][1][1])+dp[i-1][0][0]:
        dp[i][0][3] = dp[i-1][0][3] + [1]
    else:
        dp[i][0][3] = dp[i-1][1][3] + [1]
    dp[i][0][1] = [a,b]
    dp[i][0][2] = dp[i-1][0][2]
    dp[i][1][0] = min(abs(a-dp[i-1][0][2][0])+abs(b-dp[i-1][0][2][1])+dp[i-1][0][0],abs(a-dp[i-1][1][2][0])+abs(b-dp[i-1][1][2][1])+dp[i-1][1][0])
    if dp[i][1][0]==abs(a-dp[i-1][0][2][0])+abs(b-dp[i-1][0][2][1])+dp[i-1][0][0]:
        dp[i][1][3] = dp[i-1][0][3] + [2]
    else:
        dp[i][1][3] = dp[i-1][1][3] + [2]
    dp[i][1][1] = dp[i-1][1][1]
    dp[i][1][2] = [a,b]
if dp[-1][0][0]<dp[-1][1][0]:
    print(dp[-1][0][0])
    for i in dp[-1][0][3]:
        print(i)
else:
    print(dp[-1][1][0])
    for i in dp[-1][1][3]:
        print(i)
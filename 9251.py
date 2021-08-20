a = input()
b = input()
dp = [[0,-1] for _ in range(len(a))]
# dp[i][0] : 그 문자가 마지막일 때 최적해
# dp[i][1] : LCS일 때 b의 꼬리 index
if (a[0] in b):
    dp[0][0] = 1
    dp[0][1] = b.index(a[0])
else:
    dp[0][1] = -1
for i in range(1,len(a)):
    j = i - 1
    while (j>=0):
        if (a[i] in b[dp[j][1]+1:]):
            # 최적해 갱신?
            if (dp[i][0]<dp[j][0]+1):
                dp[i][0] = dp[j][0]+1
                dp[i][1] = b[dp[j][1]+1:].index(a[i]) + dp[j][1] + 1
        j-=1
print(max(dp)[0])
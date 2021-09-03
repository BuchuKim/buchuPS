import sys;read=sys.stdin.readline
a = read().rstrip()
b = read().rstrip()
len_a,len_b = len(a),len(b)
dp = [[0 for _ in range(len_b)] for _ in range(len_a)]
for i in range(len_a):
    if (a[i]==b[0]):
        dp[i][0] = 1
    else:
        if (i>0):
            dp[i][0] = dp[i-1][0]
for i in range(len_b):
    if (b[i]==a[0]):
        dp[0][i] = 1
    else:
        if (i>0):
            dp[0][i] = dp[0][i-1]
for i in range(1,len_a):
    for j in range(1,len_b):
        if (a[i]!=b[j]):
            dp[i][j] = max(dp[i][j-1],dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j-1] + 1
print(dp[len_a-1][len_b-1])
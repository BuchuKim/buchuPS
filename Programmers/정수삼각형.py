def solution(triangle):
    dp = [[0 for _ in range(i)] for i in range(1,len(triangle)+1)]

    # base case
    dp[0] = [triangle[0][0]]
    for i in range(1,len(triangle)):
        dp[i][0] = dp[i-1][0] + triangle[i][0]

    for i in range(1,len(triangle)):
        for j in range(1,len(triangle[i])-1):
            dp[i][j] = max(dp[i-1][j-1],dp[i-1][j]) + triangle[i][j]
        dp[i][-1] = dp[i-1][-1] + triangle[i][-1]

    return max(dp[-1])

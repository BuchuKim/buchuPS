import sys;read=sys.stdin.readline
INF = sys.maxsize
n = int(read())
room = list(map(int, read().split()))
m = int(read())

# dp[i] : 예산 i로 할 수 있는 최대의 방번호.
dp = [-INF for _ in range(m+1)]
for i in range(n-1, -1, -1):
    # 큰 숫자부터 비용을 가져온다
    x = room[i]
    for j in range(x, m+1):
        # 현재 고려중인 숫자 : i
        # 1. 현재 숫자 비용(x)을 쓰지 않았을 때 있던 숫자 + 끝에 현재 숫자를 붙인 숫자
        # 2. 현재 숫자 i (base case)
        # 3. 나자신. dp[j-x]가 -inf 일수도 있기 때문.
        dp[j] = max(dp[j-x]*10+i, i, dp[j])

print(dp[m])
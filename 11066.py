import sys; read = sys.stdin.readline

def dp(start,end):
        if d[start][end] != -1:
            # 들린적 O
            return d[start][end]
        if start == end:
            # base
            return 0
        
        ans = sys.maxsize
        s = sum(arr[start:end+1])
        for i in range(start, end):
        	# 모든 분할 지점에 대하여, 양분할 한 것 각각 + 둘을 합친 것이 총 비용
            temp = dp(start,i) + dp(i+1,end) + s
            ans = min(temp,ans)
            d[start][end] = ans
        return ans

for i in range(int(read())):
    n = int(read())
    arr = list(map(int,read().split()))
    d = [[-1 for _ in range(n)] for _ in range(n)]
    
    print(dp(0,n-1))
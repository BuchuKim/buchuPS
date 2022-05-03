import sys;read=sys.stdin.readline
N = int(read())
R = [0 for _ in range(N)]
G = [0 for _ in range(N)]
B = [0 for _ in range(N)]
for i in range(N):
    R[i],G[i],B[i] = map(int,read().split())

# rdp[r][i] : 처음이 r일 때, i번째 집을 r로 칠했을 때 최소비용
rdp = [[10000001 for _ in range(N)] for _ in range(3)]
rdp[0][0] = R[0]
gdp = [[10000001 for _ in range(N)] for _ in range(3)]
gdp[1][0] = G[0]
bdp = [[10000001 for _ in range(N)] for _ in range(3)]
bdp[2][0] = B[0]
for i in range(1,N):
    for j in range(3):
        # 처음 칠한 집이 j일 때, i번째 집을 r/g/b로 칠했을 때 최소비용
        rdp[j][i] = min(gdp[j][i-1],bdp[j][i-1]) + R[i]
        gdp[j][i] = min(rdp[j][i-1],bdp[j][i-1]) + G[i]
        bdp[j][i] = min(gdp[j][i-1],rdp[j][i-1]) + B[i]
ans = 1000000
for i in range(3):
    if (i==0):
        ans = min(ans,gdp[i][-1],bdp[i][-1])
    elif (i==1):
        ans = min(ans,rdp[i][-1],bdp[i][-1])
    else:
        ans = min(ans,rdp[i][-1],gdp[i][-1])
print(ans)
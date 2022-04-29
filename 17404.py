import sys;read=sys.stdin.readline
N = int(read())
R = [0 for _ in range(N)]
G = [0 for _ in range(N)]
B = [0 for _ in range(N)]
for i in range(N):
    R[i],G[i],B[i] = map(int,read().split())
rdp = [sys.maxsize] * N
rdp[0] = R[0]
gdp = [sys.maxsize] * N
gdp[0] = G[0]
bdp = [sys.maxsize] * N
bdp[0] = B[0]
for i in range(1,N-1):
    rdp[i] = min(gdp[i-1],bdp[i-1]) + R[i]
    gdp[i] = min(rdp[i-1],bdp[i-1]) + G[i]
    bdp[i] = min(gdp[i-1],rdp[i-1]) + B[i]
rdp[N-1] = min()
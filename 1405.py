import sys;input=sys.stdin.readline
N,e,w,s,n = map(int,input().split())
e,w,s,n = e/100, w/100, s/100, n/100

dx,dy,dp = [0,0,-1,1], [-1,1,0,0], [s,n,w,e]
ans = 0

def isValid(x,y):
    return 0<=x,y<2*N+1

def search(x:int,y:int,c:int,path:set,p:float):
    global ans
    if (c==N):
        ans += p
        return
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if isValid(nx,ny) and (nx,ny) not in path:
            newPath = set(path)
            newPath.add((nx,ny))
            search(nx,ny,c+1,newPath,p*dp[i])

search(N,N,0,set([(N,N)]),1)
print(ans)
from collections import deque
n = int(input())

# 1 더하거나
# 2 곱하거나
# 3 곱함
def search(N):
    visited = [0 for _ in range(N+1)]
    num = 1
    bfsQ = deque([[num,0]])
    visited[1] = 1
    while (bfsQ):
        V = bfsQ.popleft()
        if (V[0]+1<=N and visited[V[0]+1]==0):
            if (V[0]+1==N):
                return V[1]+1
            visited[V[0]+1]=1
            bfsQ.append([V[0]+1,V[1]+1])
        if (V[0]*2<=N and visited[V[0]*2]==0):
            if (V[0]*2==N):
                return V[1]+1
            visited[V[0]*2]=1
            bfsQ.append([V[0]*2,V[1]+1])
        if (V[0]*3<=N and visited[V[0]*3]==0):
            if (V[0]*3==N):
                return V[1]+1
            visited[V[0]*3]=1
            bfsQ.append([V[0]*3,V[1]+1])
        

if (n==1):
    print(0)
else:
    print(search(n))

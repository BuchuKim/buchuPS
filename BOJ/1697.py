from collections import deque
N,K = map(int,input().split())

# 1. 앞으로 가거나
# 2. 뒤로 가거나
# 3. 순간이동을 하거나!
def search(N,K):
    visited = [0 for _ in range(1000001)]
    bfsQ = deque()
    bfsQ.append([N,0])
    visited[N]=1
    while (len(bfsQ)>0):
        N = bfsQ.popleft()
        if (visited[N[0]+1]==0 and N[0]+1<=100000):
            if (N[0]+1==K):
                return N[1]+1
            bfsQ.append([N[0]+1,N[1]+1])
            visited[N[0]+1]=1
        if (visited[N[0]-1]==0 and N[0]-1>=0):
            if (N[0]-1==K):
                return N[1]+1
            bfsQ.append([N[0]-1,N[1]+1])
            visited[N[0]-1]=1
        if (visited[N[0]*2]==0 and N[0]*2<=100000):
            if (N[0]*2==K):
                return N[1]+1
            bfsQ.append([N[0]*2,N[1]+1])
            visited[N[0]*2]=1

if (N==K):
    print(0)
else:
    print(search(N,K))
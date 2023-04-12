import sys;read=sys.stdin.readline
from collections import deque
N = int(read())

space = [[] for _ in range(N)]
current = []
big = 2
ate = 0
ans = 0

for i in range(N):
    space[i] = list(map(int,read().split()))
    for j in range(N):
        if space[i][j]==9:
            current = [i,j]

def isValid(V):
    return 0<=V[0]<N and 0<=V[1]<N
def search(V):
    global big, ate, ans, space, current
    # 왼쪽 위부터 탐색하기위한..
    dx = [-1,0,0,1]
    dy = [0,-1,1,0]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    bfsQ = deque()
    bfsQ.append(V)
    while bfsQ:
        V = bfsQ.popleft()
        visited[V[0]][V[1]] = 1
        for i in range(4):
            newV = [V[0]+dx[i],V[1]+dy[i]]
            if (isValid(newV) and visited[newV[0]][newV[1]]==0 and space[newV[0]][newV[1]]<=big):
                # 이곳으로 이동할 수 있어
                bfsQ.append(newV)
                if (0<space[newV[0]][newV[1]]<big):
                    print(newV)
                    # 먹을 수 있어 -> 바로 가서 먹어!
                    ate+=1
                    space[newV[0]][newV[1]] = 0
                    ans = ans + abs(newV[0]-current[0]) + abs(newV[1]-current[1])
                    current[0] = newV[0]
                    current[1] = newV[1]
                    if (ate==big):
                        # 진화!
                        ate = 0
                        big += 1
                    return True
        
    # 더이상 먹을 수 있는곳 X
    return False

while search(current):
    continue
print(ans)
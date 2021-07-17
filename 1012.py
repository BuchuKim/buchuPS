import sys
T = int(sys.stdin.readline())
def search(_visited,_graph,V,M,N):
    if (V in _visited or _graph[V[0]][V[1]]==0):
        # 이미 들린 곳 혹은 배추가 없는 곳
        return
    bfsQ = [V]
    while (len(bfsQ)>0):
        V = bfsQ.pop(0)
        if (V[0]>=N or V[0]<0 or V[1]>=M or V[1]<0 or (V in _visited) or _graph[V[0]][V[1]]==0):
            continue
        _visited.append(V)
        left = [V[0],V[1]-1]
        right = [V[0],V[1]+1]
        up = [V[0]-1,V[1]]
        down = [V[0]+1,V[1]]
        bfsQ.append(left)
        bfsQ.append(right)
        bfsQ.append(up)
        bfsQ.append(down)
    return _visited

for _ in range(T):
    # m: 가로길이, n: 세로길이
    m,n,k = map(int,sys.stdin.readline().split())
    graph = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        a,b = map(int,sys.stdin.readline().split())
        graph[b][a] = 1
    answer = 0
    visited = []
    for i in range(n):
        for j in range(m):
            v = [i,j] # 정상적인 좌표
            before = len(visited)
            search(visited,graph,v,m,n)
            if (before<len(visited)):
                answer += 1
    print(answer)

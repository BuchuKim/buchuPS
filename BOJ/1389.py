from sys import stdin

N,M = map(int,stdin.readline().split())

friends = [[0 for _ in range (N+1)] for _ in range(N+1)]

for _ in range(M):
    a,b = map(int,stdin.readline().split())
    friends[a][b] = friends[b][a] = 1

def search(V,_visited):
    answer = 0
    _visited.append(V)
    bfsQ = [[V,0]]
    while bfsQ:
        V,breadth = bfsQ.pop(0)
        for i in range(1,N+1):
            if (friends[V][i]==1 and i not in _visited):
                bfsQ.append([i,breadth+1])
                _visited.append(i) 
                answer += breadth+1
    return answer

currentMin = N*N
answer = 0
for i in range(1,N+1):
    visited = []
    cur = search(i,visited)
    if (cur<currentMin):
        currentMin = cur
        answer = i
print(answer)
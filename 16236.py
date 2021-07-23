N = int(input())
graph = [] # 수족관
sharkindex = [0,0] # 상어 위치
shark = 2 # 상어크기
ate = 0 # 상어가 먹은 물고기 수
answer = 0
for i in range(N):
    l = list(map(int,input().split()))
    if (9 in l):
        sharkindex[0] = i
        sharkindex[1] = l.index(9)
        l[sharkindex[1]] = 0
    graph.append(l)

def isValid(V):
    return (0<=V[0]<N and 0<=V[1]<N)
def findFish(_graph,V):
    visited = [[0 for _ in range(N)] for _ in range(N)]
    bfsQ = [V]
    while bfsQ:
        V = bfsQ.pop(0)
        visited[V[0]][V[1]] = 1
        # 상 - 좌 - 우 - 하 순으로 탐색
        if (isValid([V[0]-1,V[1]]) and visited[V[0]-1][V[1]]==0):
            if (_graph[V[0]-1][V[1]]!= 0 and _graph[V[0]-1][V[1]]<shark):
                _graph[V[0]-1][V[1]] = 0
                return [V[0]-1,V[1]]
            if (_graph[V[0]-1][V[1]]<=shark):
                bfsQ.append([V[0]-1,V[1]]) # 비었거나, 비지 않았는데 상어보다 크거나.
        if (isValid([V[0],V[1]-1]) and visited[V[0]][V[1]-1]==0):
            if (_graph[V[0]][V[1]-1]!=0 and _graph[V[0]][V[1]-1]<shark):
                _graph[V[0]][V[1]-1] = 0
                return [V[0],V[1]-1]
            if (_graph[V[0]][V[1]-1]<=shark):
                bfsQ.append([V[0],V[1]-1])
        if (isValid([V[0],V[1]+1]) and visited[V[0]][V[1]+1]==0):
            if (_graph[V[0]][V[1]+1]!=0 and _graph[V[0]][V[1]+1]<shark):
                _graph[V[0]][V[1]+1] = 0
                return [V[0],V[1]+1]
            if (_graph[V[0]][V[1]+1]<=shark):
                bfsQ.append([V[0],V[1]+1])
        if (isValid([V[0]+1,V[1]]) and visited[V[0]+1][V[1]]==0):
            if (_graph[V[0]+1][V[1]]!=0 and _graph[V[0]+1][V[1]]<shark):
                _graph[V[0]+1][V[1]] = 0
                return [V[0]+1,V[1]]
            if (_graph[V[0]+1][V[1]]<=shark):
                bfsQ.append([V[0]+1,V[1]])
    return [-1,-1]

while True:
    fish = findFish(graph,sharkindex)
    if (fish==[-1,-1]):
        break
    print("current shark:",sharkindex)
    print("fish:",fish)
    answer += abs(fish[0]-sharkindex[0]) + abs(fish[1]-sharkindex[1])
    print("now, shark swim",answer)
    ate += 1
    if (ate==shark):
        shark += 1
        ate = 0
    sharkindex = fish

print(answer)
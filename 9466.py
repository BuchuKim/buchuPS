import sys;read=sys.stdin.readline

def dfs(v):
    global answer
    visited[v] = True
    cycle.append(v)
    if (not visited[arr[v]]):
        dfs(arr[v])
    else:
        if (arr[v] in cycle):
            answer += cycle[cycle.index(arr[v]):]
            return
for _ in range(int(read())):
    N = int(read())
    arr = [0] + list(map(int,read().split()))
    answer = []
    visited = [False] * (N+1)
    for i in range(1,N+1):
        if (not visited[i]):
            cycle = []
            dfs(i)
    print(N-len(answer))
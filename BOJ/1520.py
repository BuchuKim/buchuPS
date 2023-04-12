import sys;read=sys.stdin.readline
sys.setrecursionlimit(10 ** 8)
m,n = map(int,read().split())
graph = []
for _ in range(m):
    graph.append(list(map(int,read().split())))
dx = [-1,1,0,0]
dy = [0,0,-1,1]
# visited는 -1으로 초기화
visited = [[-1 for _ in range(n)] for _ in range(m)]
def search(x,y):
    if x==m-1 and y==n-1:
        # 목적 좌표에 닿았을 때 -> 여기까지 올 수 있음
        return 1
    if visited[x][y] != -1:
        # 한 번 방문한 적 있음 -> 그 노드에서 출발해서 얻을 수 있는 경우의 수 return
        return visited[x][y]
    # 방문한적 없음 -> 방문 표시
    visited[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0<=nx<m and 0<=ny<n and graph[nx][ny]<graph[x][y]):
            # 가능한 각각의 새로운 좌표에 대해서 경우의 수를 더해준다.
            visited[x][y] += search(nx,ny)
    return visited[x][y]
print(search(0,0))
import sys;read=sys.stdin.readline
sys.setrecursionlimit(int(10))
R,C = map(int,read().split())
dx = [1,-1,0,0]
dy = [0,0,1,-1]
graph = []
for _ in range(R):
    graph.append(list(read().rstrip()))
maxalp = 0
def search(a,b,alp):
    global visited,maxalp
    maxalp = max(len(alp),maxalp)
    for i in range(4):
        x = a + dx[i]
        y = b + dy[i]
        if (0<=x<R and 0<=y<C):
            if (graph[x][y] not in alp):
                search(x,y,alp+graph[x][y])
search(0,0,graph[0][0])
print(maxalp)
import sys;read=sys.stdin.readline
R,C = map(int,read().split())
dx = [1,-1,0,0]
dy = [0,0,1,-1]
graph = []
ans = 0
alp = set()
for _ in range(R):
    graph.append(list(read().rstrip()))
def search(a,b,cnt):
    global ans
    ans = max(ans,cnt)
    for i in range(4):
        a_n = a + dx[i]
        b_n = b + dy[i]
        if (0<=a_n<R and 0<=b_n<C and graph[a_n][b_n] not in alp):
            al = graph[a_n][b_n]
            alp.add(al)
            search(a_n,b_n,cnt+1)
            alp.remove(al) # 백트래킹
alp.add(graph[0][0])
search(0,0,1)
print(ans)
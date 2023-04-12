import sys
N = int(sys.stdin.readline())
graph = []
for _ in range(N):
    graph.append(list(map(int,sys.stdin.readline().split())))
answer = [0,0]
def same(_i,_j,n):
    # 모든 종이가 같은 색을 가지는지?
    a = graph[_i][_j]
    for i in range(n):
        for j in range(n):
            if (graph[_i+i][_j+j]!=a):
                return False
    return True
def search(_i,_j,n):
    # i,j : 좌표, n: 한 변의 크기
    if same(_i,_j,n):
        answer[graph[_i][_j]] += 1
        return
    for i in range(2):
        for j in range(2):
            search(_i+(n//2)*i,_j+(n//2)*j,n//2)
search(0,0,N)
for i in answer:
    print(i)
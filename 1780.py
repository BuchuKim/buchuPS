N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int,input().split())))
answer = [0,0,0]

def isDone(_i,_j,_n):
    a = graph[_i][_j]
    for i in range(_i,_n+_i):
        for j in range(_j,_n+_j):
            if (graph[i][j]!=a):
                return False
    return True

def search(_i,_j,_n):
    if (isDone(_i,_j,_n)):
        answer[graph[_i][_j]] += 1
        return
    for i in range(3):
        for j in range(3):
            search(_i+i*(_n//3),_j+j*(_n//3),_n//3)

search(0,0,N)
print(answer[2])
print(answer[0])
print(answer[1])
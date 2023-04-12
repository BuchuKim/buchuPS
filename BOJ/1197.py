import sys;read=sys.stdin.readline
V,E = map(int,read().split())
graph = []
for _ in range(E):
    a,b,c = map(int,read().split())
    graph.append([c,a,b])
graph.sort(key=lambda x:x[0])
arr = [i for i in range(V+1)]
def find(x):
    while arr[x]!=x:
        x = arr[x]
    return x
def union(x,y):
    x = find(x)
    y = find(y)
    if (x==y):
        return False
    else:
        if (x>y):
            arr[x] = y
        else:
            arr[y] = x
        return True
answer = []
for c,a,b in graph:
    if (union(a,b)):
        answer.append(c)
print(sum(answer))
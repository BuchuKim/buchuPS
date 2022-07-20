import sys;input=sys.stdin.readline
def find(x):
    p = parent[x]
    while parent[p]!=p:
        p = parent[p]
    parent[x] = p
    return p
def union(x,y):
    x,y = find(x),find(y)
    if x<y:
        parent[y] = x
        network[x] += network[y]
        return network[x]
    elif x>y:
        parent[x] = y
        network[y] += network[x]
        return network[y]
    else:
        return network[x]
for _ in range(int(input())):
    f = int(input())
    ID = {}
    parent = [i for i in range(2*f+1)]
    network = [1 for _ in range(2*f+1)]
    i = 0
    for _ in range(f):
        a,b = input().split()
        if a not in ID:
            ID[a] = i
            i += 1
        if b not in ID:
            ID[b] = i
            i += 1
        print(union(ID[a],ID[b]))
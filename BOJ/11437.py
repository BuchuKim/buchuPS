import sys;input=sys.stdin.readline

def setNode(v,l):
    # 특정 노드의 level과 parent 설정
    visited[v] = True
    level[v] = l
    for n_v in tree[v]:
        if not visited[n_v]:
            parent[n_v] = v
            setNode(n_v,l+1)

def search(a,b):
    # 높이 맞춰주기
    while level[a]!=level[b]:
        if level[a]>level[b]:
            a = parent[a]
        else:
            b = parent[b]
    # a,b에서 시작해 부모 같아질 때까지 부모로 올림
    while a!=b:
        a,b = parent[a][0],parent[b][0]
    return a

n = int(input())
tree = [[] for _ in range(n+1)]
parent = [0 for _ in range(n+1)]
level = [0 for _ in range(n+1)]
visited = [False for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)
setNode(1,0)
for _ in range(int(input())):
    a,b = map(int,input().split())
    print(search(a,b))

import sys;read=sys.stdin.readline

def searchChild(N):
    ret = 0
    if children[N][0]!=-1:
        ret += searchChild(children[N][0]) + 1
    if children[N][1]!=-1:
        ret += searchChild(children[N][1]) + 1
    return ret
def leveling(N,lev):
    level[lev].append(N)
    l,r = children[N]
    if l!=-1:
        leveling(l,lev+1)
    if r!=-1:
        leveling(r,lev+1)
def left_calc(N):
    l,r = children[N]
    if l!=-1:
        if children[l][1]!=-1:
            left[l] = left[N] - (searchChild(children[l][1])+1) -1
        else:
            left[l] = left[N] -1
        left_calc(l)
    if r!=-1:
        if children[r][0]!=-1:
            left[r] = 1 + left[N] + (searchChild(children[r][0]) + 1)
        else:
            left[r] = 1 + left[N]
        left_calc(r)

n = int(read())
children = [0 for _ in range(n+1)]
parent = [-1 for _ in range(n+1)]
left = [-1 for _ in range(n+1)]
level = [[] for _ in range(n+1)]
for _ in range(n):
    p,l,r = map(int,read().split())
    children[p] = [l,r]
    if l!=-1:
        parent[l] = p
    if r!=-1:
        parent[r] = p
root = parent[1:].index(-1)+1
left[root] = searchChild(children[root][0])+1
leveling(root,1)
left_calc(root)

ans = 1
ans_i = 1
for i in range(2,n+1):
    if not level[i]:
        break
    if left[level[i][-1]]-left[level[i][0]]+1>ans:
        ans_i = i
        ans = left[level[i][-1]]-left[level[i][0]]+1
print(ans_i, ans)
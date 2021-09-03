import sys; read=sys.stdin.readline
sys.setrecursionlimit(100000)
N = int(read())
inorder = list(map(int,read().split()))
postorder = list(map(int,read().split()))
tree = {}
def search2(start,end,pstart,pend):
    if (end-start==1):
        return inorder[start]
    elif (end-start==0):
        return 0
    root = postorder[pend-1]
    tree[root] = [0,0]
    index = inorder.index(root)
    step = index - start
    tree[root][0] = search2(start,start+step,pstart,pstart+step)
    tree[root][1] = search2(start+step+1,end,pstart+step,pend-1)
    return root
search2(0,N,0,N)
# 프리오더 출력
def pre(root):
    print(root,end=' ')
    if (root not in tree):
        return
    if (tree[root][0]!=0):
        pre(tree[root][0])
    if (tree[root][1]!=0):
        pre(tree[root][1])
pre(postorder[-1])
print()
# 1부터 N까지 중복 없는 트리
import sys; read=sys.stdin.readline
N = int(read())
sys.setrecursionlimit(100000)
inorder = list(map(int,read().split()))
postorder = list(map(int,read().split()))
tree = {}
in_location = [0 for _ in range(N+1)]
for i in range(1,N):
    in_location[inorder[i]] = i
def search2(start,end,pstart,pend):
    if (end-start==1):
        print(inorder[start],end=' ')
        return
    elif (end-start==0):
        return 0
    root = postorder[pend-1]
    print(root,end=' ')
    tree[root] = [0,0]
    index = in_location[root]
    step = index - start
    tree[root][0] = search2(start,start+step,pstart,pstart+step)
    tree[root][1] = search2(start+step+1,end,pstart+step,pend-1)
search2(0,N,0,N)
print()
"""
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
"""
"""
15
8 4 9 2 10 5 11 1 12 6 13 3 14 7 15
8 9 4 10 11 5 2 12 13 6 14 15 7 3 1

5
4 2 1 3 5
4 2 5 3 1
"""
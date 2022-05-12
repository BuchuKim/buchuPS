import sys;input=sys.stdin.readline

def findChild(p,i):
    if len(p)==1:
        return
    left_num = i.index(p[0])
    if left_num>0:
        tree[p[0]][0] = p[1]
        findChild(p[1:left_num+1],i[:left_num])
    if len(p)>left_num+1:
        tree[p[0]][1] = p[left_num+1]
        findChild(p[left_num+1:],i[left_num+1:])
def postorder(node):
    if tree[node][0]!=0:
        postorder(tree[node][0])
    if tree[node][1]!=0:
        postorder(tree[node][1])
    print(node,end=" ")

for _ in range(int(input())):
    n = int(input())
    tree = [[0,0] for _ in range(n+1)]
    preorder = list(map(int,input().split()))
    inorder = list(map(int,input().split()))
    findChild(preorder,inorder)
    root = preorder[0]
    postorder(root)
    print()
    
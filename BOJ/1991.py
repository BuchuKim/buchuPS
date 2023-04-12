import sys
read = sys.stdin.readline
N = int(read())
tree = {}
for _ in range(N):
    p,l,r = read().split()
    tree[p] = [0,0]
    if (l!="."):
        tree[p][0] = l
    if (r!="."):
        tree[p][1] = r

def jeon(V):
    print(V,end='')
    left = tree[V][0]
    right = tree[V][1]
    if (left!=0):
        jeon(left)
    if (right!=0):
        jeon(right)
def joong(V):
    left = tree[V][0]
    right = tree[V][1]
    if (left!=0):
        joong(left)
    print(V,end='')
    if (right!=0):
        joong(right)
def hoo(V):
    left = tree[V][0]
    right = tree[V][1]
    if (left!=0):
        hoo(left)
    if (right!=0):
        hoo(right)
    print(V,end='')

jeon('A')
print()
joong('A')
print()
hoo('A')
print()
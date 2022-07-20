import sys;input=sys.stdin.readline
n = int(input())
gool = {}
for _ in range(n):
    food = list(input().split())[1:]
    cur = gool
    for f in food:
        if f not in cur:
            cur[f] = {}
        cur = cur[f]
    cur[0] = True # leaf

def search(cur,level):
    if 0 in cur:
        return
    child = sorted(cur)
    for f in child:
        print('--'*level+f)
        search(cur[f],level+1)
search(gool,0)
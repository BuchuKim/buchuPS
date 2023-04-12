import sys;input=sys.stdin.readline
sys.setrecursionlimit(10**6)

pre = []
while True:
    try:
        pre.append(int(input()))
    except:
        break

def search(s,e):
    if s==e:
        return
    div = e
    for i in range(s+1,e):
        if pre[i]>pre[s]:
            div = i
            break
    search(s+1,div)
    search(div,e)
    print(pre[s])

search(0,len(pre))
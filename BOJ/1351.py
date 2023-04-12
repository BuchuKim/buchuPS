import sys;input=sys.stdin.readline
n,p,q = map(int,input().split())
moohan = {0:1}
def search(i):
    if i in moohan:
        return moohan[i]
    a,b = i//p,i//q
    if a not in moohan:
        moohan[a] = search(a)
    if b not in moohan:
        moohan[b] = search(b)
    moohan[i] = moohan[a]+moohan[b]
    return moohan[i]
print(search(n))
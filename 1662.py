import sys;input=sys.stdin.readline
string = input().rstrip()

def search(coef,idx):
    curlen = 0
    idx += 1
    while idx<len(string) and string[idx]!=")":
        if string[idx]=="(":
            c,idx = search(int(string[idx-1]),idx)
            curlen += c-1
        else:
            curlen+=1
            idx += 1
    return curlen * coef, idx+1

print(search(1,-1)[0])
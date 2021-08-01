import sys
N = int(sys.stdin.readline())
_ = sys.stdin.readline()
broken = list(sys.stdin.readline().split())
avail = set(['0','1','2','3','4','5','6','7','8','9'])
for i in broken:
    avail.remove(i)
curmin = abs(N-100)
answeri = 0
for i in range(1000000):
    channel = str(i)
    for j in range(len(channel)):
        if channel[j] not in avail:
            break
        elif (j==len(channel)-1):
            pushed = len(channel) + abs(N-i)
            curmin = min(curmin,pushed)
print(curmin)
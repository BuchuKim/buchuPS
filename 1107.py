import sys
N = int(sys.stdin.readline())
_ = sys.stdin.readline()
broken = list(map(int,sys.stdin.readline().split()))
avail = [0,1,2,3,4,5,6,7,8,9]
for i in broken:
    avail.remove(i)

def making(_num):
    # avail로 만들 수 있는 num에 가장 가까운! 숫자.
    snum = str(_num)
    click = 0
    current = 100
    curmin = abs(_num-current)
    for s in snum:
        n = int(s)
        
    return click



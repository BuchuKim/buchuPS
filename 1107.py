import sys
N = int(sys.stdin.readline())
_ = sys.stdin.readline()
broken = list(map(int,sys.stdin.readline().split()))
avail = [0,1,2,3,4,5,6,7,8,9]
for i in broken:
    avail.remove(i)

def making(_avail,_num):
    # avail로 만들 수 있는 num에 가장 가까운! 숫자.
    currentmin = int(_num)
    answer = ''
    return answer

# 버튼을 최소 몇 번 눌러야 하는지?
current = 100
click = 0
# 1. 남은 숫자를 이용해서 N과 가장 가까운 숫자를 만든 뒤에
# 2. +-를 이용하자
while (current!=N):
    # 무식한 +-질
    click = abs(current-N)
    n = str(N)
    cur = ''


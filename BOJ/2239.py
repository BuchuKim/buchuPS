# 2239 : 스도쿠
import sys;read=sys.stdin.readline
sudoku = []
for _ in range(9):
    li = list(map(int,list(read().rstrip())))
    sudoku.append(li)
def box(a,b):
    x,y = a//3, b//3
    a = sudoku[x:x+3]
    b = []
    for i in range(3):
        b += a[i][y:y+3]
    return set(b)
def possible(a,b):
    # (a,b)에서 가능한 모든 숫자 나옴
    ans = []
    for i in range(1,10):
        if (i in sudoku[a]):
            continue
        if i in list(sudoku[j][b] for j in range(9)):
            continue
        if (i in box(a,b)):
            continue
        ans.append(i)
    return ans
can = [[[] for _ in range(9)] for _ in range(9)]
def search():
    # 가능한 모든 숫자 업데이트..
    for i in range(9):
        for j in range(9):
            if (sudoku[i][j]==0):
                can[i][j] = possible(i,j)
def update():
    # can updater : 한 개만 있거나 가능한게 나밖에 없으면 update
    altered = False
    for i in range(9):
        for j in range(9):
            if (sudoku[i][j]!=0):
                continue
            if (len(can[i][j])==1):
                altered = True
                sudoku[i][j] = can[i][j].pop()
            else:
                for n in can[i][j]:
                    # n이 유일한 애인지 확인
                    only = True
                    for li in (can[i][_j] for _j in range(9)):
                        if n in li:
                            only = False
                            break
                    if not only:
                        continue
                    for li in (can[_i][j] for _i in range(9)):
                        if n in li:
                            only = False
                            break
                    if not only:
                        continue
                    _i = i//3
                    _j = j//3
                    a = can[_i:i+3]
                    b = []
                    for i in range(3):
                        b.append(a[i][_j:_j+3])
                    for li in (b[k] for k in range(3)):
                        if n in li:
                            only = False
                            break
                    if only:
                        altered = True
                        sudoku[i][j] = n
                        can[i][j] = []
                search()
    return altered
def finished():
    for li in sudoku:
        if 0 in li:
            return False
    return True
def paint():
    for li in sudoku:
        for i in li:
            print(i,end='')
        print()
search()
while True:
    al = update()
    if finished():
        break
    if not al:
        paint()
        for i in range(9):
            for j in range(9):
                if (sudoku[i][j]==0):
                    sudoku[i][j] = can[i][j].pop(0)
        search()
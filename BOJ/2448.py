n = int(input())

tri = [[' ' for _ in range(2*n)] for _ in range(n)]
def paint(n,V):
    # 대각선 한 변의 길이가 n, 위 꼭짓점 좌표가 V인 삼각형 그리기!
    if (n==3): # base case
        tri[V[0]][V[1]] = '*'
        tri[V[0]+1][V[1]+1] = '*'
        tri[V[0]+1][V[1]-1] = '*'
        tri[V[0]+2][V[1]-2] = '*'
        tri[V[0]+2][V[1]-1] = '*'
        tri[V[0]+2][V[1]] = '*'
        tri[V[0]+2][V[1]+1] = '*'
        tri[V[0]+2][V[1]+2] = '*'
        return
    else:
        paint(n//2,V)
        paint(n//2,[V[0]+n//2,V[1]-n//2])
        paint(n//2,[V[0]+n//2,V[1]+n//2])
paint(n,[0,n-1])
for i in tri:
    for j in i:
        print(j,end='')
    print()
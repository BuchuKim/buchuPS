def solution(board, skill):
    answer = 0
    n,m = len(board),len(board[0])
    accum = [[0 for _ in range(m+1)] for _ in range(n+1)]

    for isAttack,r1,c1,r2,c2,degree in skill:
        degree = -degree if isAttack==1 else degree
        accum[r1][c1] += degree
        accum[r2+1][c1] -= degree
        accum[r1][c2+1] -= degree
        accum[r2+1][c2+1] += degree
        
    for x in range(n+1):
        for y in range(1,m+1):
            accum[x][y] += accum[x][y-1]

    for y in range(m+1):
        for x in range(1,n+1):
            accum[x][y] += accum[x-1][y]

    for x in range(n):
        for y in range(m):
            if (board[x][y] + accum[x][y]>0):
                answer += 1

    return answer
result = 0
def search(N,A):
    # N : 크기
    # A : 현재 사각형의 왼쪽 위 (n,m)
    global result
    if (A[0]==r and A[1]==c):
        print(int(result))
        exit(0)
    if (N==1):
        # 한개 블록
        result += 1
        return result
    # 구하고자 하는게 범위 안에 없음
    if not (A[0] <= r < A[0]+N and A[1] <= c < A[1]+N):
        result += N*N
        return result
    search(N/2,A)
    search(N/2,[A[0],A[1]+N/2])
    search(N/2,[A[0]+N/2,A[1]])
    search(N/2,[A[0]+N/2,A[1]+N/2])

n,r,c = map(int,input().split())
search(2**n,[0,0])
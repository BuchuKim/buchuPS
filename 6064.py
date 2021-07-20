def sol(m,n,x,y):
    answer = x
    while True:
        if (answer > m*n):
            return -1
        else:
            if ((answer-y)%n ==0):
                return answer
        answer += m

T = int(input())
for _ in range(T):
    m,n,x,y = map(int,input().split())
    print(sol(m,n,x,y))
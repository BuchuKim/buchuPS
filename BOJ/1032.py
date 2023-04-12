M,N = map(int,input().split())

def check(arr):
    # 왼쪽 위를 'W'로 만드는 경우
    # get 8*8 block
    ans1 = 0 # 왼쪽 위가 'W'인 경우
    ans2 = 0 # 왼쪽 위가 'B'인 경우
    for i in range(8):
        for j in range(8):
            # WBWBWB...
            if (i%2==0 and j%2==0):
                # 짝수번째 줄 : 짝수번째가 W
                if (arr[i][j]=='B'):
                    ans1 += 1
            elif (i%2==0 and j%2==1):
                if (arr[i][j]=='W'):
                    ans1 += 1
            elif (i%2==1 and j%2==0):
                # 홀수번째 줄 : 짝수번째가 B
                if (arr[i][j]=='W'):
                    ans1 += 1
            else:
                if (arr[i][j]=='B'):
                    ans1 += 1

            # BWBWBWBW...
            if (i%2==0 and j%2==0):
                # 짝수번째 줄 : 짝수번째가 W
                if (arr[i][j]=='W'):
                    ans2 += 1
            elif (i%2==0 and j%2==1):
                if (arr[i][j]=='B'):
                    ans2 += 1
            elif (i%2==1 and j%2==0):
                # 홀수번째 줄 : 짝수번째가 B
                if (arr[i][j]=='B'):
                    ans2 += 1
            else:
                if (arr[i][j]=='W'):
                    ans2 += 1
    return min(ans1,ans2)



board = []
# M 단위로 받음 (2중 list)
for i in range(M):
    a = []
    for s in input():
        a.append(s)
    board.append(a)

answer = M*N # initial : max
for i in range(M-7):
    for j in range(N-7):
        inputboard = [] # 8*8
        for k in range(8):
            a = board[i+k]
            a = a[j:j+8]
            inputboard.append(a)
        answer = min(answer,check(inputboard))
print(answer)
        

N = int(input())
stair = [int(input()) for _ in range(N)]
answer = [stair[0],stair[0]+stair[1]]
answer.append(max(stair[0]+stair[2],stair[1]+stair[2]))
for i in range(3,N):
    answer.append(max(answer[i-3]+stair[i-1]+stair[i],answer[i-2]+stair[i]))
print(answer[-1])
N = int(input())
l = list(map(int,input().split()))
l.sort()
answer = 0
for i in range(N):
    answer += l[i]*(N-i)
print(answer)
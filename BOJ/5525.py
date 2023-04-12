N = int(input())
M = int(input())
S = input()
answer = 0

p = "I"
for _ in range(N):
    p += "OI"

for i in range(M-(2*N+1)):
    if (S[i:i+(2*N)+1]==p):
        answer += 1

print(answer)
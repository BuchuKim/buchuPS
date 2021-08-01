# 사람수 N, 파티수 M. 사람 번호는 1번부터 N번까지
# 둘째 줄에는 진실을 아는 사람 번호가 주어짐
# 셋째 줄부터 M번째 줄까지는 각 파티에 오는 사람수!
from sys import stdin
N,M = map(int,stdin.readline().split())
truth = set(list(map(int,stdin.readline().split()))[1:])
answer = 0
for _ in range(M):
    came = set(list(map(int,stdin.readline().split()))[1:])
    can = True
    for i in came:
        if i in truth:
            can = False
            break
        else:
            truth.add(i)
    if can: answer += 1
print(answer)
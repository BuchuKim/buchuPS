# 9095
T = int(input())
answer = [0,1,2,4]
for i in range(4,11):
    answer.append(answer[i-1]+answer[i-2]+answer[i-3])

for _ in range(T):
    n = int(input())
    print(answer[n])
# answer[k]
# answer[k-1] 에서 1이 하나 더 늘어남.... 
# answer[k-2] 에서 1이 두개 더 늘어남 / 2가 한 개 더 늘어남
# answer[k-3] 에서 1이 세개 더 늘어남 / 3이 한 개 더 늘어남 / 1과 2가 한개씩 더 늘어남
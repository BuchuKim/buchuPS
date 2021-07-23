# 1931
N = int(input())
answer = 0
times = []
for _ in range(N):
    s,e = map(int,input().split())
    times.append([s,e])
times.sort(key=lambda x : (x[1],x[0]))

end = 0
for i in range(len(times)):
    if (times[i][0]>=end):
        answer += 1
        end = times[i][1]
print(answer)
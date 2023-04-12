# 사람수 N, 파티수 M. 사람 번호는 1번부터 N번까지
# 둘째 줄에는 진실을 아는 사람 번호가 주어짐
# 셋째 줄부터 M번째 줄까지는 각 파티에 오는 사람수!
from sys import stdin; read=stdin.readline
N,M = map(int,read().split())
tpeople = set(list(map(int,read().split()))[1:])
graph = [[0 for _ in range(N+1)] for _ in range(N+1)]
partygraph = []
def search(V):
    for i in range(1,N+1):
        if (graph[V][i]==1 and (i not in tpeople)):
            tpeople.add(i)
            search(i)
for _ in range(M):
    party = list(map(int,read().split()))[1:]
    partygraph.append(party)
    for i in range(len(party)-1):
        for j in range(i+1,len(party)):
            graph[party[i]][party[j]] = 1
            graph[party[j]][party[i]] = 1
t = list(tpeople)
for v in t:
    search(v)

answer = 0
for i in partygraph:
    can = True
    for p in i:
        if p in tpeople:
            can = False
        break
    if can:
        answer += 1
print(answer)
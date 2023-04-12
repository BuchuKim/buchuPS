N = int(input())

people =[]
for _ in range(N):
    people.append(list(map(int,input().split())))
for p1 in people:
    ranking = 1
    for p2 in people:
        if (p2[0]>p1[0] and p2[1]>p1[1]):
            ranking += 1
    p1.append(ranking)

for p in people:
    print(p[2],end=' ')
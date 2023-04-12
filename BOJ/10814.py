import sys
n = int(sys.stdin.readline())

people = []
for _ in range(n):
    person = list(sys.stdin.readline().split())
    person[0] = int(person[0])
    people.append(person)
people.sort(key=lambda x:x[0])

for i in people:
    print(i[0],i[1],sep=' ')
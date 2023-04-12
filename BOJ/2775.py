T = int(input())

def people(a,b):
    building = [[i for i in range(1,b+1)]]
    # 1,2,3, ..., b
    for i in range(1,a+1):
        section = [1]
        for j in range(1,b):
            section.append(section[j-1]+building[i-1][j])
        building.append(section)
    return building[a][b-1]

for _ in range(T):
    k = int(input())
    n = int(input())
    print(people(k,n))
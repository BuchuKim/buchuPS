import sys
read = sys.stdin.readline

N = int(read())
tri = []
for i in range(N):
    tri.append(list(map(int,read().split())))
# 밑에서부터 올라와
for i in range(1,N):
    for j in range(len(tri[i])):
        if (j==0):
            tri[i][j] += tri[i-1][j]
        elif (j==len(tri[i])-1):
            tri[i][j] += tri[i-1][j-1]
        else:
            tri[i][j] += max(tri[i-1][j],tri[i-1][j-1])
print(max(tri[N-1]))
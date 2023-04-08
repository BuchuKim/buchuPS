import sys;input=sys.stdin.readline
D,N = map(int,input().split())
R = list(map(int,input().split()))
pizza = list(map(int,input().split()))

for i in range(D-1):
    if R[i+1]>R[i]:
        R[i+1] = R[i]

p = 0
for i in range(D-1,-1,-1):
    # i : 현재 피자가 들어갈 수 있는 오븐 index
    if (pizza[p] > R[i]):
        continue

    p += 1
    if p==N:
        print(i+1)
        sys.exit(0)

print(0)
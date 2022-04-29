import sys;read=sys.stdin.readline

N = int(read())

chu = list(map(int,read().split()))
chu.sort()

can = [0 for _ in range(sum(chu)+1)]
can[0] = 1
can[chu[0]] = 1
for i in range(N):
    # 현재 저울에 올라간 가장 작은 추가 chu[i]일 때
    
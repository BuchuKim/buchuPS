import sys;input=sys.stdin.readline
n = int(input())
score = {}
for _ in range(n):
    num = input().rstrip()
    for i in range(1,len(num)+1):
        s = num[len(num)-i]
        if s not in score:
            score[s] = [0,0]
        score[s][1] += 36**(i-1)
k = int(input())

pair = {}
for i in range(10):
    pair[str(i)] = i
for i in range(65,91):
    pair[chr(i)] = i-55

for s in score:
    score[s][0] = 35*score[s][1]-pair[s]*score[s][1]
score = sorted(score.items(), key=lambda x: (-x[1][0],x[0]))
ans = 0
i = 0
for key,(_,value) in score:
    if i<k:
        ans += value * 35
        if key=='Z':
            continue
    else:
        ans += pair[key] * value
    i += 1

def to35(N):
    ret = []
    while N//36>0:
        na = N%36
        if na<10:
            ret.append(str(na))
        else:
            ret.append(chr(na+55))
        N //= 36
    na = N%36
    if na<10:
        ret.append(str(na))
    else:
        ret.append(chr(na+55))
    ret.reverse()
    return "".join(ret)

print(to35(ans))
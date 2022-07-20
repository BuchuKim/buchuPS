import sys;read=sys.stdin.readline
N = int(read())
words = []
for _ in range(N):
    words.append(read().rstrip())
score = {}
notzero = set()
for w in words:
    for i in range(len(w)):
        if i==0:
            notzero.add(w[i])
        if w[i] in score:
            score[w[i]] += 10**(len(w)-i-1)
        else:
            score[w[i]] = 10**(len(w)-i-1)
arr = []
ans = 0
for s in score:
    arr.append([score[s],s])
if len(arr)==10:
    # 0먼저 찾고시작
    arr.sort()
    for i in range(10):
        if arr[i][1] not in notzero:
            del arr[i]
            break
arr.sort(reverse=True)
a = 9
ans = 0
for i in range(len(arr)):
    ans += a*arr[i][0]
    a -= 1
print(ans)
import sys;read=sys.stdin.readline
N = int(read())
words = []
alp_score = {}
for _ in range(N):
    w = list(read().rstrip())
    words.append(w)
    for i in range(len(w)):
        if w[i] in alp_score:
            alp_score[w[i]] += 10 ** (len(w)-i-1)
        else:
            alp_score[w[i]] = 10 ** (len(w)-i-1)
alps = []
for alp in alp_score:
    alps.append([alp_score[alp],alp])
alps.sort(reverse=True)
s = 9
for _,a in alps:
    alp_score[a] = s
    s-=1
ans = 0
for w in words:
    for i in range(len(w)):
        ans += alp_score[w[i]] *10 ** (len(w)-i-1)
print(ans)
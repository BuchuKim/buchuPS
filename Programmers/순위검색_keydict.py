from itertools import combinations
from collections import defaultdict
from bisect import bisect_left

def solution(info,query):
    dict,ans = defaultdict(list),[]
    for i in info:
        i = i.split()
        condition,score = i[:-1],int(i[-1])
        for i in range(5):
            wild_idx = list(combinations([0,1,2,3],i))
            for wi in wild_idx:
                tmp = condition.copy()
                for idx in wi:
                    tmp[idx] = "-"
                key = "".join(tmp)
                dict[key].append(score)
    
    for scores in dict.values():
        scores.sort()
    
    for q in query:
        q = [c for c in q.split(" ") if c!="and"]
        key = "".join(q[:-1])
        qscore = int(q[-1])

        if (key in dict):
            scores = dict[key]
            ans.append(len(scores)-bisect_left(scores,qscore))
        else:
            ans.append(0)
    
    return ans

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(info,query))

from bisect import bisect_left
def solution(info, query):
    ans = []
    graph = {} # store score
    for lang in ("java","python","cpp"):
        graph[lang] = {}
        for field in ("backend","frontend"):
            graph[lang][field] = {}
            for year in ("junior","senior"):
                graph[lang][field][year] = {}
                for food in ("chicken","pizza"):
                    graph[lang][field][year][food] = []
    
    for i in info:
        lang,field,year,food,score = i.split()
        graph[lang][field][year][food].append(int(score))
    
    for q in query:
        qlang,_,qfield,_,qyear,_,qfood,qscore = q.split()
        qlang = [qlang] if qlang!="-" else ["java","python","cpp"]
        qfield = [qfield] if qfield!="-" else ["backend","frontend"]
        qyear = [qyear] if qyear!="-" else ["junior","senior"]
        qfood = [qfood] if qfood!="-" else ["chicken","pizza"]

        scores = []
        for lang in qlang:
            for field in qfield:
                for year in qyear:
                    for food in qfood:
                        scores += graph[lang][field][year][food]
        
        scores.sort()

        ans.append(len(scores)-bisect_left(scores,int(qscore)))

    return ans


info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(info,query))
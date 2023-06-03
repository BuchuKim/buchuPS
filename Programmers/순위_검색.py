from bisect import bisect_left
def solution(info, query):
    ans,people = [],[]
    for p in info:
        lang,field,career,food,s = p.split()
        s = int(s)
        people.append([s,lang,field,career,food])
    people.sort()
    score = [p[0] for p in people]
    
    for q in query:
        q_lang,_,q_field,_,q_career,_,q_food,q_score = q.split()
        q_score = int(q_score)
        
        # cut_index부터 살펴봄
        cut_index,pass_num = bisect_left(score,q_score),0
        for i in range(cut_index,len(score)):
            _,cur_lang,cur_field,cur_career,cur_food = people[i]
            if (q_lang!="-" and q_lang!=cur_lang):
                continue
            if (q_field!="-" and q_field!=cur_field):
                continue
            if (q_career!="-" and q_career!=cur_career):
                continue
            if (q_food!="-" and q_food!=cur_food):
                continue
                
            # 모든 조건 만족
            pass_num += 1
            
        ans.append(pass_num)
    return ans
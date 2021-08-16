def search(arr,tofind):
    start = 0
    end = len(arr)-1
    while (start<=end):
        mid = (start + end) // 2
        if (arr[mid][0]<tofind):
            start = mid + 1
        else:
            end = mid - 1
    return start
def solution(info, query):
    answer = []
    for i in range(len(info)):
        l,j,k,f,s = info[i].split()
        info[i] = [int(s),l,j,k,f]
    info.sort(key=lambda x : x[0])
    print(info)
    for q in query:
        # l: lang, j:jikgun, k:kyeong, f: food, s: score
        hap = 0
        l,_,j,_,k,_,f,s = q.split()
        index = search(info,int(s))
        while (index<len(info)):
            if (((l!="-" and info[index][1]==l) or l=="-") and ((j!="-" and info[index][2]==j) or j=="-") and ((k!="-" and info[index][3]==k) or k=="-") and ((f!="-" and info[index][4]==f) or f=="-")):
                hap += 1
            index += 1
        answer.append(hap)
    return answer

print(solution(["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"], ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]))
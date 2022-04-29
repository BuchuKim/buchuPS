def solution(record):
    answer = []
    pair = {}
    for r in record:
        arr = r.split()
        pair[arr[1]] = arr[2]
    for r in record:
        arr = r.split()
        if (arr[0]=="Enter"):
            answer.append(pair[arr[1]]+"님이 들어왔습니다.")
        elif (arr[0]=="Leave"):
            answer.append(pair[arr[1]]+"님이 나갔습니다.")
    return answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))
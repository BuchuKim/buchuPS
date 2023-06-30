def add_month(year,month,add):
    month += add
    while (month>12):
        year += 1
        month -= 12
    return year,month

def solution(today, terms, privacies):
    answer = []
    t_year,t_month,t_day = map(int,today.split("."))
    policy = {}
    for t in terms:
        name,month = t.split(" ")
        policy[name] = int(month)
    for i in range(len(privacies)):
        date,term = privacies[i].split(" ")
        ex_year,ex_month,ex_day = map(int,date.split("."))
        ex_year,ex_month = add_month(ex_year,ex_month,policy[term])
        if (t_year<ex_year):
            continue
        if (t_year==ex_year and t_month<ex_month):
            continue
        if (t_year==ex_year and t_month==ex_month and t_day < ex_day):
            continue
        answer.append(i+1)
    return answer
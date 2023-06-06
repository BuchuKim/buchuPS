def solution(enroll, referral, seller, amount):
    children,money = {p:set() for p in enroll},{p:0 for p in enroll}
    parent = {enroll[i]:referral[i] for i in range(len(enroll))}

    for i in range(len(enroll)):
        if referral[i]!="-":
            children[referral[i]].add(enroll[i])

    for i in range(len(seller)):
        person, profit = seller[i], amount[i]*100
        while (person!="-"):
            money[person] += profit
            up = int(profit * 0.1)
            if (up==0):
                break
            money[person] -= up
            profit = up
            person = parent[person]

    return [money[p] for p in enroll]
        
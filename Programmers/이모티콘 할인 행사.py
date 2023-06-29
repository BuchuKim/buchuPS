from itertools import product
def solution(users, emoticons):
    n,m = len(users),len(emoticons)
    ans_reg,ans_amount = -1,-1

    sales = product((10,20,30,40),repeat=m)
    for sale in sales:
        cur_reg = 0 # 지금 이 할인율에서의 가입자
        user_purchase_amount = [0 for _ in range(n)] # 각 유저의 구매 금액

        for i in range(m):
            price = emoticons[i] * (1-(sale[i]*0.01))
            for j in range(n):
                if (users[j][0]<=sale[i]):
                    user_purchase_amount[j] += price
        
        for i in range(n):
            if (user_purchase_amount[i] >= users[i][1]):
                user_purchase_amount[i] = 0
                cur_reg += 1
        
        if (cur_reg<ans_reg):
            continue
        elif (cur_reg>ans_reg):
            ans_reg = cur_reg
            ans_amount = sum(user_purchase_amount)
        else:
            ans_amount = max(ans_amount,sum(user_purchase_amount))

    return [ans_reg,int(ans_amount)]


print(solution([[40, 10000], [25, 10000]],[7000, 9000]))
print(solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]],[1300, 1500, 1600, 4900]))
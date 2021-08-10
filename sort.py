print('이 프로그램은 당신의 취향을 분석해서 프린트해줍니다!')
print('소트하고자 하는 취향들을 쭉 적고, 슬래시 \'/\' 로 나눠주세요!')
toSort = list(input().split('/'))
prior = []
for s in toSort:
    prior.append([0,s])
while True:
    for i in range(1,len(prior)):
        if (prior[i][1]==prior[0][1]):
            a = prior[i][0]
            b = prior[0][0]
            try:
                c = input(a,'vs',b,": ")
                break
            except (c!=a and c!=b):
                print("a와 b중에 고르셔야죠~")
            except:
                print('뭐가 잘못된 것 같거든요? 다시 해주세요.')
            if (c==a):
                prior[i][1] += 1
            else:
                prior[0][1] += 1
    

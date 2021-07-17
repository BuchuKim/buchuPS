# 다음 -가 나올 떼가지 -뒤에 있는 것들은 전부! 음수로 만들면 되는거 아녀?!
ex = input()
num = ''
nums=[]
op = []
for i in range(len(ex)):
    if (ex[i] in "0123456789"):
        num += ex[i]
    else:
        nums.append(int(num))
        num=''
        op.append(ex[i])
nums.append(int(num))
answer = nums[0]

opIndex = 0
while (opIndex<len(op)):
    if (op[opIndex]=="+"):
        answer += nums[opIndex+1]
        opIndex += 1
    else:
        while (opIndex<len(op)):
            answer -= nums[opIndex+1]
            opIndex += 1

print(answer)
import sys
n = int(sys.stdin.readline())
done = True
answer = []
stacks = []
curnum = 1
    
for i in range(n):
    num = int(sys.stdin.readline())
    if (curnum<=num):
        stacks.append(curnum)
        answer.append('+')
        curnum += 1
        while(curnum<=num):
            # 그 num에 닿을 때까지 push
            stacks.append(curnum)
            answer.append('+')
            curnum += 1
        stacks.pop()
        answer.append('-')
    else:
        # curnum > num
        if (stacks[-1]!=num):
            done = False
            break
        else:
            stacks.pop()
            answer.append('-')

if (done):
    for s in answer:
        print(s)
else:
    print('NO')
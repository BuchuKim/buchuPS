from collections import deque
inputStr = input()
answer = []
while (inputStr!='.'):
    q = deque()
    success = True
    for s in inputStr:
        if (s in "(["):
            q.append(s)
        elif (s==")"):
            if (len(q)==0):
                answer.append('no')
                success = False
                break
            if (q.pop()!="("):
                answer.append('no')
                success = False
                break
        elif (s=="]"):
            if (len(q)==0):
                answer.append('no')
                success = False
                break
            if (q.pop()!="["):
                answer.append('no')
                success = False
                break
    if (success):
        if (len(q)!=0):
            answer.append('no')
        else:
            answer.append('yes')
    inputStr = input()

for s in answer:
    print(s)
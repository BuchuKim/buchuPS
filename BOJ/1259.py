# (x,y) : 현재 위치
# (w,h) : 꼭짓점
x,y,w,h = map(int,input().split())
answer = []
answer.append(x)
answer.append(y)
answer.append(abs(w-x))
answer.append(abs(h-y))
print(min(answer))
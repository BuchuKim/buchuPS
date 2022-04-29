import sys; read=sys.stdin.readline
from collections import deque
n = int(read())
crane = list(map(int,read().split()))
m = int(read())
box = list(map(int,read().split()))

crane.sort(reverse=True)
box.sort(reverse=True)
box = deque(box)
# print("crane:",crane)
# print("box:",list(box))

# corner case : 가장 큰 crane보다 가장 큰 box가 크면 아예 불가능
if (crane[0]<box[0]):
    print(-1)
    exit()

ans = 1
while len(box)>0:
    # print(ans,":",end=' ')
    # print(list(box))
    new_box = deque()
    for i in range(n):
        if (crane[i]>=box[0]):
            box.popleft()
        else:
            if (crane[i]<box[-1]):
                # crane[i]가 가장 작은 box보다 작다면... 이번 iter은 그름
                break
            while (crane[i]<box[0]):
                # crane[i]가 담을 수 있는 box가 나올때까지 뒤로 미뤄
                new_box.append(box.popleft())
            box.popleft()
        if (len(box)==0):
            break
    box = list(box+new_box)
    box.sort(reverse=True)
    box = deque(box)
    if (len(box)==0):
        print(ans)
        exit()
    ans += 1
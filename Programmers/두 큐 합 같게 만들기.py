from collections import deque
def solution(queue1, queue2):
    sum1,sum2 = sum(queue1),sum(queue2)
    if (sum1+sum2)%2==1:
        return -1
    
    count,max_count = 0,len(queue1)*2+2
    queue1,queue2 = deque(queue1),deque(queue2)
    while (count <= max_count):
        if (sum1>sum2):
            # 1->2
            popped = queue1.popleft()
            queue2.append(popped)
            sum1 -= popped
            sum2 += popped
        elif (sum1<sum2):
            # 2->1
            popped = queue2.popleft()
            queue1.append(popped)
            sum2 -= popped
            sum1 += popped
        else:
            return count
        count += 1
    return -1
from collections import deque
def solution(cap, n, deliveries, pickups):
    answer = 0
    deliveries, pickups = deque((i+1,deliveries[i]) for i in range(n)),deque((i+1,pickups[i]) for i in range(n))

    # 배달할 곳에 쭉 배달한 다음 수거하는 전략
    while (deliveries or pickups):
        cur_dis = 0
        # 1. 배달가야지
        remain = cap
        while (deliveries and remain>0):
            dis,box = deliveries.popleft()
            cur_dis = max(cur_dis,dis)
            if (remain < box):
                # 더 못담아
                deliveries.appendleft((dis,box-remain))
                break
            else:
                remain -= box

        # 2. 수거해야지
        remain = cap
        while (pickups and remain>0):
            dis,box = pickups.popleft()
            cur_dis = max(cur_dis,dis)
            if (remain < box):
                pickups.appendleft((dis,box-remain))
                break
            else:
                remain -= box
        
        answer += cur_dis * 2

    return answer
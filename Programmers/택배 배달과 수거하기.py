from heapq import heappop,heappush,heapify
def solution(cap, n, deliveries, pickups):
    answer = 0
    deliver, pickup = [],[]
    for i in range(n):
        if (deliveries[i]!=0):
            deliver.append((-i-1,deliveries[i]))
        if (pickups[i]!=0):
            pickup.append((-i-1,pickups[i]))
    heapify(deliver); heapify(pickup)

    # 배달할 곳에 쭉 배달한 다음 수거하는 전략
    while (deliver or pickup):
        cur_dis = 0
        # 1. 배달가야지
        remain = cap
        while (deliver and remain>0):
            dis,box = heappop(deliver)
            cur_dis = max(cur_dis,-dis)
            if (remain < box):
                # 더 못담아
                heappush(deliver,(dis,box-remain))
                break
            else:
                remain -= box

        # 2. 수거해야지
        remain = cap
        while (pickup and remain>0):
            dis,box = heappop(pickup)
            cur_dis = max(cur_dis,-dis)
            if (remain < box):
                heappush(pickup,(dis,box-remain))
                break
            else:
                remain -= box

        answer += cur_dis * 2

    return answer
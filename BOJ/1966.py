def whenPrinted(arr,index):
    answer = 0 # print 될때마다 늘어남
    curIndex = index # 우리가 print하고자 하는 원소가 현재 있는 위치
    done = False
    while True:
        if (max(arr)<=arr[0]):
            # print it (큐 맨 앞이 가장 높은 우선순위)
            answer += 1
            del(arr[0])
            if (curIndex==0):
                # 만약 큐 가장 앞의 원소가 우리가 원하는 원소였을때 -> 멈춤.
                break
            # 맨 앞이 없어졌으므로 curIndex 하나 줄어듦
            curIndex -= 1
        else:
            # there are higher priority
            arr.append(arr[0])
            del(arr[0])
            if (curIndex == 0):
                # 맨 앞이 우리가 원한는 거였을 때 -> 큐 맨 뒤로 보내버려
                curIndex = len(arr)-1
            else:
                curIndex -= 1
    return answer
        

T = int(input())

for i in range(T):
    N,M = map(int,input().split())
    prior = list(map(int,input().split()))
    print(whenPrinted(prior,M))

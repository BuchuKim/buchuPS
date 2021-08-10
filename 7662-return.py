from sys import stdin; read=stdin.readline
import heapq
T = int(read())
for _ in range(T):
    k = int(read())
    # visited : 이 아이디를 가진 노드가 삭제되었는지, 그렇지 않은지 판단하는 식별자
    visited = [0 for _ in range(1000001)]
    # 일단 두 개의 큐가 필요.
    minQ = []
    maxQ = []
    for i in range(k):
        op, n = stdin.readline().split()
        n = int(n)
        if (op=="I"):
            heapq.heappush(minQ,(n,i))
            heapq.heappush(maxQ,(-n,i))
            visited[i] = 1 # visited[i]=1을 해주는 이유 -> 이 노드는 현재 들어있는 노드라는 뜻
        elif (n==1): # 최댓값을 빼라.
            # maxQ에 원소가 있고, 삭제되어있는 노드라면? -> 쓰레기 노드들이잖아. 싹다 삭제시켜-!
            while maxQ and visited[maxQ[0][1]]==0:
                heapq.heappop(maxQ)
            if maxQ:
                # 위 while로 쓰레기노드들은 다 삭제된 상태임. 이제 maxQ의 첫번째 원소, 즉 가장 큰 원소를 "진짜" pop할 차례.
                # visited[maxQ[0][1]] 해줌으로서 minQ에 이 노드가 삭제된 노드임을 알리고, 실제로 팝한다.
                visited[maxQ[0][1]] = 0
                heapq.heappop(maxQ)
        else:
            # 역시 가장 작은걸 빼라 할 때, minQ의 쓰레기 노드들을 싹다 삭제한다.
            while minQ and visited[minQ[0][1]]==0:
                heapq.heappop(minQ)
            if minQ:
                # 그 뒤 minQ[0][1] id를 가진 visited를 0으로 바꿔 이게 삭제된 노드임을 알린다.
                # 그 뒤 진짜! 팝한다.
                visited[minQ[0][1]] = 0
                heapq.heappop(minQ)
    # 마지막 max와 min에서 쓰레기 노드들을 싹다 삭제한다
    while maxQ and visited[maxQ[0][1]]==0:
        heapq.heappop(maxQ)
    while minQ and visited[minQ[0][1]]==0:
        heapq.heappop(minQ)
    if maxQ and minQ:
        print(-maxQ[0][0],minQ[0][0])
    else:
        print("EMPTY")
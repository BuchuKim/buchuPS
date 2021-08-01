from sys import stdin
import heapq
T = int(stdin.readline())
for _ in range(T):
    k = int(stdin.readline())
    Q = []
    for _ in range(k):
        op, n = stdin.readline().split()
        if (op=="I"):
            heapq.heappush(Q,int(n))
        else:
            if (n=="1"):
                if Q:
                    Q.sort()
                    Q.pop()
                    heapq.heapify(Q)
            else:
                if Q:
                    heapq.heappop(Q)
    if Q:
        Q.sort()
        print(Q[0],Q[-1])
    else:
        print("EMPTY")

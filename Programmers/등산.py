from collections import defaultdict
from heapq import heappop,heappush
def solution(n, paths, gates, summits):
    answer = [50_000,10_000_000]
    summits,gates,path = set(summits),set(gates),defaultdict(list)
    for i,j,w in paths:
        path[i].append((w,j)); path[j].append((w,i))
        
    intensities = [10_000_001 for _ in range(n+1)]
    heap,visited = [(0,s) for s in gates],[False for _ in range(n+1)]
    while heap:
        dis,node = heappop(heap)
        visited[node] = True
        if (dis > answer[1]):
            continue
            
        for n_dis,n_node in path[node]:
            if visited[n_node] or n_node in gates:
                continue
            intensity = max(n_dis,dis)
            if (intensities[n_node] > intensity):
                intensities[n_node] = intensity
                if (n_node in summits):
                    if (intensity < answer[1]):
                        answer = [n_node,intensity]
                    elif (intensity==answer[1]):
                        answer[0] = min(answer[0],n_node)
                else:
                    heappush(heap,(intensity,n_node))    
    return answer
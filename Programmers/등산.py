from collections import defaultdict,deque
import sys
def solution(n, paths, gates, summits):
    # 출입구 -> 한 번 산봉우리 -> 출입구에서 intensity 최소
    answer = [-1,sys.maxsize] # [산봉우리 번호, intensity] return
    path,gates,summits = defaultdict(list),set(gates),set(summits)
    for i,j,w in paths:
        path[i].append((j,w))
        path[j].append((i,w))

    Q = deque()
    for gate in gates:
        Q.append((gate,0,set([gate])))
    
    # BFS
    while Q:
        cur,intensity,visited = Q.popleft()
        for node,dis in path[cur]:
            if (node in visited) or (node in gates):
                continue
                
            c_intensity = max(dis,intensity)
            if node in summits:
                if (c_intensity<answer[1]):
                    answer = [node,c_intensity]
                elif (c_intensity==answer[1]):
                    answer[0] = min(node,answer[0])
                continue
            
            n_visited = set(visited); n_visited.add(node)
            Q.append((node,c_intensity,n_visited))
    return answer

def print_hang(li):
    for l in li:
        print(l)
    
    print()

def solution(rows, columns, queries):
    answer = []
    graph,c = [[] for _ in range(rows)],1
    for i in range(rows):
        for _ in range(columns):
            graph[i].append(c)
            c += 1
    
    print_hang(graph)
    for x1,y1,x2,y2 in queries:
        x1 -= 1
        y1 -= 1
        x2 -= 1
        y2 -= 1
        res = graph[x1][y1]
        
        # 맨 윗줄을 오른쪽으로
        tmp = graph[x1][y1]
        for y in range(y1,y2):
            t = graph[x1][y+1]
            res = min(t,res)
            graph[x1][y+1] = tmp
            tmp = t
        # tmp : 오른쪽 위 모서리
        
        # 맨 오른쪽 줄을 아래로
        for x in range(x1,x2):
            t = graph[x+1][y2]
            res = min(t,res)
            graph[x+1][y2] = tmp
            tmp = t
        # tmp : 오른쪽 아래 모서리
        
        # 맨 아래줄을 왼쪽으로
        tmp2 = graph[x2][y1]
        res = min(res,tmp2)
        for y in range(y1,y2-1):
            res = min(res,graph[x2][y])
            graph[x2][y] = graph[x2][y+1]
        res = min(res,graph[x2][y2-1])
        graph[x2][y2-1] = tmp
        # tmp2 : 왼쪽 아래 모서리

        # 맨 왼쪽 줄을 위로
        for x in range(x1,x2-1):
            res = min(res,graph[x][y1])
            graph[x][y1] = graph[x+1][y1]
        res = min(res,graph[x2-1][y1])
        graph[x2-1][y1] = tmp2

        print_hang(graph)
        answer.append(res)
    return answer

print(solution(3,4,[[1,1,3,4]]))

print(solution(4,3,[[1,1,4,3]]))
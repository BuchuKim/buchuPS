down,up = {},{}
def solution(info, edges):
    answer = 0
    for i in range(len(info)):
        down[i], up[i] = [],[]
    for s,e in edges:
        down[s].append(e)
        up[e].append(s)
    print(down,up)
    return answer

print(solution([0,0,1,1,1,0,1,0,1,0,1,1],[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))
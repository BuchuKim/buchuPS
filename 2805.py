def totalTree(arr,h):
    answer = 0
    for i in arr:
        if (i-h>0):
            # 나무 높이가 h보다 높아야 잘림.
            answer += i-h
    return answer

n,m = map(int,input().split())
trees = list(map(int,input().split()))
start = 0
end = max(trees)
while (start<=end):
    mid = (start+end)//2
    if (totalTree(trees,mid)>=m):
        # 많음 -> 높이 줄여!
        start = mid + 1
    else:
        # 부족 -> 높이를 좀 더 줄이자
        end = mid - 1
print(start)
print(end)
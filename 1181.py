# k개 랜선 존재, n개 만들고 싶음
k,n = map(int,input().split())
lengths = []

for i in range(k):
    lengths.append(int(input()))

# 길이의 최소, 최댓값
start = 1
end = max(lengths)

while (start<=end):
    mid = (start+end)//2
    made = 0
    for l in lengths:
        made += l//mid
    if (made>=n):
        # 더 많이 만들어짐. 길이를 늘려도 돼
        start = mid+1
    else:
        # 더 적게 만들어짐. 길이를 줄여야 해
        end = mid-1

print(end)

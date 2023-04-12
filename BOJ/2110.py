import sys;input=sys.stdin.readline
n,c = map(int,input().split())
x = [int(input()) for _ in range(n)]
x.sort()

# 가장 넓은 거리(=mid)를 이분탐색 할거임.
s,e,ans = 1,x[-1]-x[0],0
while s<=e:
    # mid: 거리, cur: 이전 집의 좌표, count: 공유기간 최소 거리가 mid일 때 설치할 수 있는 최대 공유기 개수
    mid,cur,count = (s+e)//2,x[0],1
    for i in range(1,n):
        if x[i] >= cur+mid:
            count += 1
            cur = x[i]
    if count>=c:
        # 더 많이 설치할 수 있어.. 그럼 거리를 더 늘려
        s = mid+1
        ans = mid
    else:
        # 이렇게 넓게 하면 공유기 설치 다 못해.. 거리 좁혀
        e = mid-1
print(ans)